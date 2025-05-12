# 配置中文字体
import base64
from io import BytesIO

import matplotlib
import pandas as pd
from flask import Flask, jsonify
from matplotlib import pyplot as plt

from chartGenerate.weather_bingzhuang import img_bingzhuang
from chartGenerate.weather_tiaoxing import img_tiaoxing
# from chartGenerate.weather_predict import weather_predict
from chartGenerate.weathertoLineChart import weathertoLineChart
from dataUtils.datatolist import csvtolist

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 也可以使用 ['SimSun'] 等其他中文字体
matplotlib.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

app = Flask(__name__)


def generate_base64(fig):
    buffer = BytesIO()
    fig.savefig(buffer, format='png')  # 保存图标到缓冲区
    buffer.seek(0)  # 重置缓冲区指针
    chart_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')  # 进行Base64编码
    plt.close(fig)
    return chart_base64


@app.route('/')
def home():
    return 'hello world'


@app.route('/chart1')
def show_chart1():
    df = pd.read_csv('./data/StephenCurry.csv')

    df.dropna(subset=["Season_year", "PTS", "Date"], inplace=True)
    df = df[(df["PTS"] >= 0)]

    df["Season"] = df["Season_year"].str[:4]

    fig1 = plt.figure(figsize=(15, 12))
    season_avg = df.groupby("Season")["PTS"].mean()
    season_avg.plot(kind="bar", color="skyblue")
    plt.title("库里各赛季场均得分", size=30)
    plt.xlabel("赛季", loc="right", size=20)
    plt.ylabel("得分", loc="top", size=20)
    plt.xticks(rotation=45, fontsize=17)
    plt.show()

    fig1.savefig("./chart/season_avg.png", format='png')

    fig2 = plt.figure(figsize=(18, 12))
    season_2013 = df[df["Season_year"] == "2012-2013"].sort_values("Date")
    plt.plot(season_2013["Date"], season_2013["PTS"], marker="o", linestyle="-", color="orange")
    plt.title("2012-2013赛季得分趋势", size=30)
    plt.xlabel("比赛日期", loc="right", size=20)
    plt.ylabel("得分", loc="top", size=20)
    dates_to_show = season_2013["Date"].iloc[::5]
    plt.xticks(dates_to_show, rotation=45, fontsize=17)
    plt.show()

    fig2.savefig("./chart/season_2013.png", format='png')

    return jsonify({
        'chart1': f'data:image/png;base64,{generate_base64(fig1)}',
        'chart2': f'data:image/png;base64,{generate_base64(fig2)}'
    })


@app.route('/chart2')
def show_chart2():
    plt1 = weathertoLineChart('./data/seattle-weather.csv', '2012-01-01', '2012-01-31')
    fig1 = plt1.gcf()
    fig1.set_size_inches(8, 4)
    plt1.tight_layout()
    fig1.savefig("./chart/weather_2012.png", format='png')
    plt1.show()

    # plt2 = weather_predict()
    # fig2 = plt2.gcf()
    # fig2.set_size_inches(8, 4)
    # plt2.tight_layout()
    # fig2.savefig("./chart/weather_predict.png", format='png')
    # plt2.show()

    return jsonify({
        'chart1': f'data:image/png;base64,{generate_base64(fig1)}',
        # 'chart2': f'data:image/png;base64,{generate_base64(fig2)}'
    })


@app.route('/chart3')
def show_chart3():
    list1 = csvtolist("./data/seattle-weather.csv")
    plt1 = img_bingzhuang(list1, 5)
    fig1 = plt1.gcf()
    fig1.set_size_inches(8, 4)
    plt1.tight_layout()
    fig1.savefig("./chart/weather_bingzhuang.png", format='png')
    plt1.show()

    plt2 = img_tiaoxing(list1, 5)
    fig2 = plt2.gcf()
    fig2.set_size_inches(8, 4)
    plt2.tight_layout()
    fig2.savefig("./chart/weather_tiaoxing.png", format='png')
    plt2.show()

    return jsonify({
        'chart1': f'data:image/png;base64,{generate_base64(fig1)}',
        'chart2': f'data:image/png;base64,{generate_base64(fig2)}'
    })


if __name__ == '__main__':
    app.run(debug=True)
