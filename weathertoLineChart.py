import matplotlib.pyplot as plt
import datatolist
import dataclean
def weathertoLineChart(filename = "seattle-weather.csv",start_time = '2012-01-01',end_time = '2012-01-31'):
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
    end = end_time.split('-')[0] + '年' + str(int(end_time.split('-')[1])) + '月' + str(int(end_time.split('-')[2])) + '日'
    plt.title("西雅图" + start + "至" + end + "最高最低气温折线图",fontsize=14)
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
    plt.ylabel("温度 (°C)",fontsize=12,loc='top')
    plt.legend(loc='best')

    return plt

def weather_choose_line(filename,start_time = '2012-01-01',end_time = '2012-01-31',index = '1'):
    dl = datatolist.datatolist((filename))
    dl = dataclean.weather_clean_MainCode(dl, start_time, end_time)  # 进行数据清洗，将日期为空或者不符合格式的日期去除
    dl = dataclean.weather_clean_data(dl, int(index))

    # 创建宋体字体对象
    plt.rcParams['font.sans-serif'] = ['SimSun']  # Windows系统
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示异常
    x = [x[0] for x in dl]                      #横坐标，日期作为x轴

    y_index = [x[int(index)] for x in dl]
    y_label = ""
    line_label = ""
    color = ""
    if index == '1':
        y_label = "毫米（mm）"
        line_label = "降水量"
        color = "skyblue"
    elif index == '2':
        y_label = "气温（℃）"
        line_label = "最高气温"
        color = "red"
    elif index == '3':
        y_label = "气温（℃）"
        line_label = "最低气温"
        color = "blue"
    elif index == '4':
        y_label = "风速（m/s）"
        line_label = "风力大小"
        color = "steelblue"

    plt.plot(x, y_index,
             color=color,
             linestyle='-',
             linewidth=2,
             marker='o',
             label=line_label)

    start = start_time.split('-')[0] + '年' + str(int(start_time.split('-')[1])) + '月' + str(int(start_time.split('-')[2])) + '日'
    end = end_time.split('-')[0] + '年' + str(int(end_time.split('-')[1])) + '月' + str(int(end_time.split('-')[2])) + '日'
    plt.title("西雅图" + start + "至" + end + line_label + "折线图",fontsize=14)
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
    plt.ylabel(y_label,fontsize=12,loc='top')
    plt.legend(loc='best')

    return plt
