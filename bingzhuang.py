#该文件适合统计文字类数据，转化为饼状图
import matplotlib.pyplot as plt
from collections import Counter
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

