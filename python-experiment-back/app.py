# 配置中文字体
import base64
from io import BytesIO

import matplotlib
from flask import Flask, jsonify, request
from matplotlib import pyplot as plt

from chartGenerate.weather_bar import img_tiaoxing
from chartGenerate.weather_line import weathertoLineChart, weather_choose_line
from chartGenerate.weather_pie import img_bingzhuang
from chartGenerate.weather_predict import weather_predict
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


@app.route('/lineChart', methods=['GET', 'POST'])
def create_line_chart():
    if request.method == 'POST':
        data = request.get_json()
        x_begin = data['xBegin']
        x_end = data['xEnd']
        y_value = data['yValue']

        plt1 = weathertoLineChart("./data/seattle-weather.csv", x_begin, x_end)
        fig1 = plt1.gcf()
        fig1.set_size_inches(8, 4)
        plt1.tight_layout()
        fig1.savefig('./chart/lineChartMaxAndMin.png', format='png')
        plt1.show()

        plt2 = weather_choose_line("./data/seattle-weather.csv", x_begin, x_end, y_value)
        fig2 = plt2.gcf()
        fig2.set_size_inches(8, 4)
        plt2.tight_layout()
        fig2.savefig('./chart/lineChart.png', format='png')
        plt2.show()

        plt3 = weather_predict()
        fig3 = plt3.gcf()
        fig3.set_size_inches(8, 4)
        plt3.tight_layout()
        fig3.savefig('./chart/lineChartPre.png', format='png')
        plt3.show()

        return jsonify({
            'chart1': f'data:image/png;base64,{generate_base64(fig1)}',
            'chart2': f'data:image/png;base64,{generate_base64(fig2)}',
            'chart3': f'data:image/png;base64,{generate_base64(fig3)}'
        })
    else:
        return 'it is not post'


@app.route('/pieChart', methods=['GET', 'POST'])
def create_pie_chart():
    if request.method == 'POST':
        data = request.get_json()
        x_begin = data['begin']
        x_end = data['end']

        list1 = csvtolist("./data/seattle-weather.csv")
        plt = img_bingzhuang(list1, x_begin, x_end, 5)
        fig = plt.gcf()
        fig.set_size_inches(8, 4)
        plt.tight_layout()
        fig.savefig('./chart/pieChart.png', format='png')
        plt.show()

        return jsonify({
            'chart': f'data:image/png;base64,{generate_base64(fig)}'
        })
    else:
        return 'it is not post'


@app.route('/barChart', methods=['GET', 'POST'])
def create_bar_chart():
    if request.method == 'POST':
        data = request.get_json()
        x_begin = data['begin']
        x_end = data['end']

        list1 = csvtolist("./data/seattle-weather.csv")
        plt = img_tiaoxing(list1, x_begin, x_end, 5)
        fig = plt.gcf()
        fig.set_size_inches(8, 4)
        plt.tight_layout()
        fig.savefig('./chart/barChart.png', format='png')
        plt.show()

        return jsonify({
            'chart': f'data:image/png;base64,{generate_base64(fig)}'
        })
    else:
        return 'it is not post'

if __name__ == '__main__':
    app.run(debug=True)
