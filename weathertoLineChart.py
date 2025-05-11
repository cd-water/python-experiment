import matplotlib.pyplot as plt
import datatolist
import dataclean
import mplcursors
def weathertoLineChart(filename,start_time = '2012-01-01',end_time = '2012-01-31'):
    dl = datatolist.datatolist((filename))
    dl = dataclean.weather_clean_MainCode(dl,start_time,end_time)  #进行数据清洗，将日期为空或者不符合格式的日期去除
    dl = dataclean.weather_clean_data(dl,2)                   #将最高气温中缺失的数据由平均值代替
    dl = dataclean.weather_clean_data(dl,3)                   #将最低气温中缺失的数据由平均值代替

    # 创建宋体字体对象
    plt.rcParams['font.sans-serif'] = ['SimSun']  # Windows系统
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示异常
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

    start = start_time.split('-')[0] + '年' + str(int(start_time.split('-')[1])) + '月' + str(int(start_time.split('-')[2])) + '日'
    end = end_time.split('-')[0] + '年' + end_time.split('-')[1] + '月' + end_time.split('-')[2] + '日'
    plt.title("某地" + start + "至" + end + "最高最低气温折线图",fontsize=14)
    plt.xlabel("日期",fontsize=12,loc='right')
    count = 0
    t = 0
    x_list = []
    t_list = []
    for x in dl:
        count += 1
        if count % 5 == 1:
            l = x[0].split('-')
            x_list.append(str(int(l[1])) + '月' + str(int(l[2])) + '日')
            t_list.append(t)
            t += 5
    plt.xticks(t_list,x_list)
    plt.ylabel("气温",fontsize=12,loc='top')
    plt.legend(loc='best')

    return plt

