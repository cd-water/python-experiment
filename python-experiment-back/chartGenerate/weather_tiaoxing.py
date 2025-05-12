from collections import Counter

from matplotlib import pyplot as plt


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
    return plt