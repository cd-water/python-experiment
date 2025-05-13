#该文件将文件特定列数据转化为条形、饼状统计图
#折线可以绘制出所有的数据
import matplotlib.pyplot as plt
from datatolist import csvtolist
from collections import Counter



#该函数统计指定列数的数据,从一个时间到另一个时间
def img_bingzhuang(list1,data1,data2,index):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    for i in range(1,len(list1)):
        if list1[i][0]==data1:
            first=i
        if list1[i][0]==data2:
            second=i
            break
    column_data = [row[index] for row in list1[first:second+1]]

# 统计频率
    counter = Counter(column_data)
    labels = list(counter.keys())
    sizes = list(counter.values())

    plt.figure(figsize=(5, 5))
    patches, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"{list1[first][0]}至{list1[second][0]}'{list1[0][index]}'数据频率分布", fontsize=15)
    plt.axis('equal')  # 保证为圆形
    plt.legend(patches, labels, title="图例", loc="best")
    return plt




#将特定列的数据统计出来并生成条形统计图
def img_tiaoxing(list1, data1,data2,index):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体

    for i in range(1, len(list1)):
        if list1[i][0] == data1:
            first = i
        if list1[i][0] == data2:
            second = i
            break
    column_data = [row[index] for row in list1[first:second + 1]]

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
    plt.title(f"{list1[first][0]}至{list1[second][0]}'{list1[0][index]}'数据频率分布", fontsize=15)
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

list1=csvtolist("seattle-weather.csv")
img_tiaoxing(list1,"2012-01-01","2013-01-02",5).show()
img_bingzhuang(list1, "2012-01-01","2012-02-01",5).show()


