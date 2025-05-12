from collections import Counter

from matplotlib import pyplot as plt


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
    return plt