# import pandas as pd
# from pygments.lexers import go
#
#
# def img_zhexian_plotly(data, index):
#     try:
#         title_col = data[0][index]
#         y_data = [float(row[index]) for row in data[1:]]
#         date_strs = [row[0] for row in data[1:]]
#     except ValueError:
#         print("指定列中包含非数值内容，无法绘制折线图")
#         return
#     except IndexError:
#         print("列索引超出范围")
#         return
#
#     # 转成 DataFrame 格式（Prophet 需要列名为 ds, y）
#     try:
#         df = pd.DataFrame({
#             'ds': pd.to_datetime(date_strs),
#             'y': y_data
#         })
#     except:
#         print("日期格式应为 YYYY-MM-DD")
#         return
#
#     # 建模与预测
#     model = Prophet()
#     model.fit(df)
#     future = model.make_future_dataframe(periods=30)  # 预测30天
#     forecast = model.predict(future)
#
#     # 绘图
#     fig = go.Figure()
#
#     # 实际数据
#     fig.add_trace(go.Scatter(
#         x=df['ds'],
#         y=df['y'],
#         mode='lines+markers',
#         name='实际值',
#         line=dict(color='blue')
#     ))
#
#     # 预测数据（未来部分）
#     fig.add_trace(go.Scatter(
#         x=forecast['ds'],
#         y=forecast['yhat'],
#         mode='lines',
#         name='预测值',
#         line=dict(color='red', dash='dash')
#     ))
#
#     fig.update_layout(
#         title=f"'{title_col}' 列的交互式折线图（Prophet 预测未来30天）",
#         xaxis_title='日期',
#         yaxis_title='值',
#         width=1000,
#         height=500
#     )
#
#     return fig
#
#
# def forecast_next_month_plot(data, index):
#     """
#     使用 Prophet 模型预测未来一个月的数据，并单独绘制预测折线图。
#
#     参数：
#     data：二维列表（第一行为标题，第一列为日期，index 为预测的列索引）
#     index：要预测的列索引（从0开始）
#     """
#     try:
#         title_col = data[0][index]
#         y_data = [float(row[index]) for row in data[1:]]
#         date_strs = [row[0] for row in data[1:]]
#     except ValueError:
#         print("指定列中包含非数值内容，无法处理")
#         return
#     except IndexError:
#         print("列索引超出范围")
#         return
#
#     try:
#         df = pd.DataFrame({
#             'ds': pd.to_datetime(date_strs),
#             'y': y_data
#         })
#     except:
#         print("日期格式应为 YYYY-MM-DD")
#         return
#
#     # 使用 Prophet 模型进行训练和预测
#     model = Prophet()
#     model.fit(df)
#
#     future = model.make_future_dataframe(periods=30)  # 向未来扩展30天
#     forecast = model.predict(future)
#
#     # 只取未来30天部分
#     last_date = df['ds'].max()
#     future_forecast = forecast[forecast['ds'] > last_date]
#
#     # 绘图
#     fig = go.Figure()
#
#     fig.add_trace(go.Scatter(
#         x=future_forecast['ds'],
#         y=future_forecast['yhat'],
#         mode='lines+markers',
#         name='预测值',
#         line=dict(color='green'),
#         hovertemplate='日期: %{x|%Y-%m-%d}<br>预测值: %{y:.2f}<extra></extra>'
#     ))
#
#     fig.update_layout(
#         title=f"'{title_col}' 列的未来30天预测图（使用 Prophet）",
#         xaxis_title='日期',
#         yaxis_title='预测值',
#         width=1000,
#         height=500
#     )
#
#     return fig