import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt



def weather_predict(key='temp_max'):
    # 1. 数据加载与预处理
    df = pd.read_csv('data/seattle-weather.csv', parse_dates=['date'], index_col='date')
    df = df[[key, 'precipitation', 'wind']]  # 选择主要特征
    df = df.resample('D').mean().ffill()  # 处理缺失日期

    # 2. 数据标准化
    scaler = MinMaxScaler(feature_range=(0,1))
    scaled_data = scaler.fit_transform(df)

    n_past = 14   # 使用过去14天数据
    n_future = 1  # 预测未来1天
    X, y = create_dataset(scaled_data, n_past, n_future)

    # 3. 数据集划分
    train_size = int(len(X)*0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # 4. LSTM模型构建
    model = Sequential()
    model.add(LSTM(64, return_sequences=True, input_shape=(n_past, X.shape[2])))
    model.add(Dropout(0.2))
    model.add(LSTM(32, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(y_train.shape[1]))
    model.compile(optimizer='adam', loss='mse')


    # 5. 模型训练
    early_stop = EarlyStopping(monitor='val_loss', patience=5)
    history = model.fit(X_train, y_train,
                        epochs=100,
                        batch_size=32,
                        validation_split=0.2,
                        callbacks=[early_stop],
                        verbose=1)

    # 6. 预测与反标准化
    y_pred = model.predict(X_test)
    y_pred_actual = scaler.inverse_transform(
        np.concatenate((y_pred,
                       np.zeros((len(y_pred), scaled_data.shape[1]-1))),
                       axis=1))[:,0]
    y_test_actual = scaler.inverse_transform(
        np.concatenate((y_test,
                       np.zeros((len(y_test), scaled_data.shape[1]-1))),
                       axis=1))[:,0]

    # 7. 评估指标
    rmse = np.sqrt(mean_squared_error(y_test_actual, y_pred_actual))
    mae = mean_absolute_error(y_test_actual, y_pred_actual)
    print(f'RMSE: {rmse:.2f}°C')    #均方根误差
    print(f'MAE: {mae:.2f}°C')      #平均绝对误差

    # 8. 可视化结果
    # 创建宋体字体对象
    if key == 'temp_max':
        key = '最高气温'
    else:
        key = '最低气温'
    plt.rcParams['font.sans-serif'] = ['SimSun']  # Windows系统
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示异常
    start_idx = n_past + train_size  # 跳过训练集和窗口期
    end_idx = start_idx + len(y_test_actual)  # 测试集长度
    test_dates = df.index[start_idx:end_idx]
    plt.figure(figsize=(15,6))
    plt.plot(test_dates,y_test_actual, label='真实' + key)
    plt.plot(test_dates,y_pred_actual, label='预测' + key)
    plt.title('天气' + key + '预测比较',fontsize=14)
    plt.xlabel('日期',loc='right',fontsize=12)
    plt.ylabel('温度 (°C)',loc='top',fontsize=12)
    plt.legend()
    return plt

#创建时间窗口数据集
def create_dataset(data, n_past, n_future):
    X, y = [], []
    for i in range(n_past, len(data)-n_future):
        X.append(data[i-n_past:i, :])
        y.append(data[i:i+n_future, 0])  # 预测temp_max
    return np.array(X), np.array(y)
