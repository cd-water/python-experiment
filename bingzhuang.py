#该文件将文件特定列数据转化为条形、饼状、折线统计图
import matplotlib.pyplot as plt
from collections import Counter
import plotly.express as px
from datatolist import csvtolist


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



def img_zhexian_plotly(data, index):
    """
    使用 Plotly 绘制指定列的交互式折线图

    参数：
    data：二维列表（第一行为标题）
    index：要绘制的列索引（从0开始）
    """

    try:
        # 获取标题名
        title_col = data[0][index]
        # 获取数值数据，跳过表头
        y_data = [float(row[index]) for row in data[1:]]
    except ValueError:
        print("指定列中包含非数值内容，无法绘制折线图")
        return
    except IndexError:
        print("列索引超出范围")
        return

    x_data = list(range(1, len(y_data) + 1))  # 行号作为 x 轴

    fig = px.line(
        x=x_data,
        y=y_data,
        labels={'x': '行号', 'y': '值'},
        title=f"'{title_col}' 列的交互式折线图"
    )
    fig.update_traces(mode='lines+markers')  # 显示线和点
    fig.update_layout(width=900, height=500)
    fig.show()



list1=csvtolist("seattle-weather.csv")
img_tiaoxing(list1,5)
img_bingzhuang(list1, 5)
img_zhexian_plotly(list1,2)

