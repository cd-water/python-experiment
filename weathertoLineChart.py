import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import datatolist

def weathertoLineChart(filename):
    # 创建宋体字体对象
    plt.rcParams['font.sans-serif'] = ['SimSun']  # Windows系统
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示异常
    dl = datatolist.datatolist(filename)[1:32]
    x = [x[0] for x in dl]
    y_high = [x[2] for x in dl]
    y_low = [x[3] for x in dl]
    plt.plot(x,y_high,
             color='red',
             marker='o',
             label ='最高气温')
    plt.plot(x, y_low,
             color='blue',
             marker='o',
             label = "最低气温")
    plt.title("某地2012年1月1日至1月31日最高最低气温折线图",fontsize=14)
    plt.xlabel("日期",fontsize=12,loc='right')
    plt.xticks([1,6,11,16,21,26,31],['1月1日','1月6日','1月11日','1月16日','1月21日','1月26日','1月31日'])
    plt.ylabel("气温",fontsize=12,loc='top')

    return plt

