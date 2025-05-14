from collections import Counter

from matplotlib import pyplot as plt


def img_bingzhuang(list1, data1, data2, index):
    plt.rcParams['font.sans-serif'] = ['SimHei']

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
    sizes = list(counter.values())

    plt.figure(figsize=(8, 6))
    patches, texts, autotexts = plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f"{list1[first][0]}至{list1[second][0]}'{list1[0][index]}'数据频率分布", fontsize=15)
    plt.axis('equal')  # 保证为圆形
    plt.legend(patches, labels, title="图例", loc="best")
    return plt
