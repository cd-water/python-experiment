#该文件将文件特定列数据转化为条形、饼状、折线统计图
#折线可以绘制出所有的数据
import matplotlib.pyplot as plt
from collections import Counter

import pandas as pd
import plotly.express as px
from prophet import Prophet
from pygments.lexers import go

from datatolist import csvtolist
import plotly.express as px
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression


#该函数统计指定列数的数据
def img_bingzhuang(list1,index):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    column_data = [row[index] for row in list1[1:]]

# 统计频率
    counter = Counter(column_data)

# 画饼状
    labels = counter.keys()
    sizes = counter.values()

    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"'{list1[0][index]}' 列的字符频率分布",fontsize=15)
    plt.axis('equal')  # 保证为圆形
    plt.show()


#将特定列的数据统计出来并生成条形统计图
def img_tiaoxing(list1, index):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
    column_data = [row[index] for row in list1[1:]]  # 获取指定列的数据（跳过标题行）

    # 统计频率
    counter = Counter(column_data)
    labels = list(counter.keys())
    counts = list(counter.values())

    # 画条形图
    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, counts, color='skyblue')

    # 在每个柱子上添加数值标签
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.3,  # 位置：柱顶稍上方
                 f'{int(height)}', ha='center', va='bottom', fontsize=10)

    # 添加标题和标签
    plt.xlabel("类别", fontsize=12)
    plt.ylabel("频数", fontsize=12)
    plt.title(f"'{list1[0][index]}' 列的字符频率分布", fontsize=15)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


#将特定列的数据做成折线统计图，并以第一列为每个折线统计图的下标
# def img_zhexian(list1, index):
#     plt.rcParams['font.sans-serif'] = ['SimHei']  # 支持中文
#
#     # 取出数据（跳过标题行），并尝试转换为数值
#     try:
#         y_data = [float(row[index]) for row in list1[1:]]
#     except ValueError:
#         print("指定列包含非数值，无法绘制折线图")
#         return
#
#     x_data = list(range(1, len(y_data) + 1))  # x轴为行号
#
#     plt.figure(figsize=(100, 100))
#     plt.plot(x_data, y_data, marker='o', color='steelblue', linestyle='-')
#
#     # 在每个点上显示具体数值
#     for x, y in zip(x_data, y_data):
#         plt.text(x, y + 0.5, f'{y:.1f}', ha='center', va='bottom', fontsize=30)
#
#     plt.xlabel("行号", fontsize=30)
#     plt.ylabel("值", fontsize=30)
#     plt.title(f"'{list1[0][index]}' 列的数据折线图", fontsize=30)
#     plt.grid(True)
#     plt.tight_layout()
#     plt.show()


# def img_zhexian_plotly(data, index):
#     """
#     使用 Plotly 绘制指定列的交互式折线图，并显示每个点对应的日期
#
#     参数：
#     data：二维列表（第一行为标题）
#     index：要绘制的列索引（从0开始）
#     """
#
#     try:
#         title_col = data[0][index]  # 取目标列的标题
#         y_data = [float(row[index]) for row in data[1:]]  # 提取 y 轴数据
#         date_data = [row[0] for row in data[1:]]  # 默认第一列为日期
#     except ValueError:
#         print("指定列中包含非数值内容，无法绘制折线图")
#         return
#     except IndexError:
#         print("列索引超出范围")
#         return
#
#     fig = px.line(
#         x=date_data,
#         y=y_data,
#         labels={'x': '日期', 'y': '值'},
#         title=f"'{title_col}' 列的交互式折线图"
#     )
#     fig.update_traces(mode='lines+markers', hovertemplate='日期: %{x}<br>值: %{y}<extra></extra>')
#     fig.update_layout(width=900, height=500)
#     fig.show()






from prophet import Prophet
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta

def img_zhexian_plotly(data, index):
    try:
        title_col = data[0][index]
        y_data = [float(row[index]) for row in data[1:]]
        date_strs = [row[0] for row in data[1:]]
    except ValueError:
        print("指定列中包含非数值内容，无法绘制折线图")
        return
    except IndexError:
        print("列索引超出范围")
        return

    # 转成 DataFrame 格式（Prophet 需要列名为 ds, y）
    try:
        df = pd.DataFrame({
            'ds': pd.to_datetime(date_strs),
            'y': y_data
        })
    except:
        print("日期格式应为 YYYY-MM-DD")
        return

    # 建模与预测
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)  # 预测30天
    forecast = model.predict(future)

    # 绘图
    fig = go.Figure()

    # 实际数据
    fig.add_trace(go.Scatter(
        x=df['ds'],
        y=df['y'],
        mode='lines+markers',
        name='实际值',
        line=dict(color='blue')
    ))

    # 预测数据（未来部分）
    fig.add_trace(go.Scatter(
        x=forecast['ds'],
        y=forecast['yhat'],
        mode='lines',
        name='预测值',
        line=dict(color='red', dash='dash')
    ))

    fig.update_layout(
        title=f"'{title_col}' 列的交互式折线图（Prophet 预测未来30天）",
        xaxis_title='日期',
        yaxis_title='值',
        width=1000,
        height=500
    )

    fig.show()




from prophet import Prophet
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

def forecast_next_month_plot(data, index):
    """
    使用 Prophet 模型预测未来一个月的数据，并单独绘制预测折线图。

    参数：
    data：二维列表（第一行为标题，第一列为日期，index 为预测的列索引）
    index：要预测的列索引（从0开始）
    """
    try:
        title_col = data[0][index]
        y_data = [float(row[index]) for row in data[1:]]
        date_strs = [row[0] for row in data[1:]]
    except ValueError:
        print("指定列中包含非数值内容，无法处理")
        return
    except IndexError:
        print("列索引超出范围")
        return

    try:
        df = pd.DataFrame({
            'ds': pd.to_datetime(date_strs),
            'y': y_data
        })
    except:
        print("日期格式应为 YYYY-MM-DD")
        return

    # 使用 Prophet 模型进行训练和预测
    model = Prophet()
    model.fit(df)

    future = model.make_future_dataframe(periods=30)  # 向未来扩展30天
    forecast = model.predict(future)

    # 只取未来30天部分
    last_date = df['ds'].max()
    future_forecast = forecast[forecast['ds'] > last_date]

    # 绘图
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=future_forecast['ds'],
        y=future_forecast['yhat'],
        mode='lines+markers',
        name='预测值',
        line=dict(color='green'),
        hovertemplate='日期: %{x|%Y-%m-%d}<br>预测值: %{y:.2f}<extra></extra>'
    ))

    fig.update_layout(
        title=f"'{title_col}' 列的未来30天预测图（使用 Prophet）",
        xaxis_title='日期',
        yaxis_title='预测值',
        width=1000,
        height=500
    )

    fig.show()




# list1=csvtolist("seattle-weather.csv")
# img_tiaoxing(list1,5)
# img_bingzhuang(list1, 5)
# img_zhexian_plotly(list1,2)
# forecast_next_month_plot(list1, 2)

