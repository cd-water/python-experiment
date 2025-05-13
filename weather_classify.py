import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import datatolist as data_util

# 配置matplotlib支持中文显示
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False  # 正确显示负号



def classify_weather(weather_data, start_date=None, end_date=None):
    """根据多列数据智能分类天气类型"""
    weather_classification = {}
    headers = weather_data[0]

    # 获取各字段索引
    date_idx = headers.index('date')
    weather_idx = headers.index('weather')
    temp_max_idx = headers.index('temp_max') if 'temp_max' in headers else None
    wind_idx = headers.index('wind') if 'wind' in headers else None
    precipitation_idx = headers.index('precipitation') if 'precipitation' in headers else None

    # 转换日期格式
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    for row in weather_data[1:]:
        row_date = datetime.strptime(row[date_idx], '%Y-%m-%d')

        # 筛选日期范围
        if start_date and row_date < start_date:
            continue
        if end_date and row_date > end_date:
            continue

        # 获取各字段值
        weather = str(row[weather_idx]).lower()
        temp_max = float(row[temp_max_idx]) if temp_max_idx is not None else None
        wind = float(row[wind_idx]) if wind_idx is not None else None
        precipitation = float(row[precipitation_idx]) if precipitation_idx is not None else None

        # 基于多条件的智能天气分类
        weather_type = None

        # 极端天气判断 (优先级最高)
        if temp_max is not None and temp_max >= 33:
            if 'sun' in weather:
                weather_type = '酷暑'
            elif 'cloud' in weather:
                weather_type = '闷热'

        if precipitation is not None and precipitation > 25:
            if wind is not None and wind > 7:
                weather_type = '暴风雨'
            else:
                weather_type = '暴雨'

        if wind is not None and wind > 12:
            weather_type = '大风'

        # 常规天气判断
        if weather_type is None:
            if 'sun' in weather:
                if temp_max is not None:
                    if temp_max >= 28:
                        weather_type = '晴热'
                    elif temp_max < 15:
                        weather_type = '晴冷'
                    else:
                        weather_type = '晴朗'
                else:
                    weather_type = '晴天'
            elif 'rain' in weather or 'drizzle' in weather:
                if precipitation is not None:
                    if precipitation < 5:
                        weather_type = '小雨'
                    elif precipitation < 15:
                        weather_type = '中雨'
                    else:
                        weather_type = '大雨'
                else:
                    weather_type = '雨天'
            elif 'fog' in weather or 'cloud' in weather or 'overcast' in weather:
                if temp_max is not None and temp_max < 10:
                    weather_type = '阴冷'
                else:
                    weather_type = '阴天'
            elif 'snow' in weather:
                weather_type = '下雪'
            else:
                weather_type = '其他'

        # 更新统计
        if weather_type in weather_classification:
            weather_classification[weather_type] += 1
        else:
            weather_classification[weather_type] = 1

    return weather_classification


def plot_pie_chart(weather_classification, title="天气类型占比饼状图"):
    """绘制带图例的饼状图"""
    # 合并数量较少的类别以提高可读性
    filtered_classes = weather_classification.copy()
    threshold = max(1, len(weather_classification) * 0.03)  # 小于3%的类别合并

    if len(weather_classification) > 6:
        other_count = 0
        for wc, count in list(filtered_classes.items()):
            if count < threshold:
                other_count += count
                del filtered_classes[wc]
        if other_count > 0:
            filtered_classes["其他"] = other_count

    labels = list(filtered_classes.keys())
    sizes = list(filtered_classes.values())

    # 定义每种天气类型的颜色
    colors = {
        '晴天': '#FFD700',  # 金色
        '晴热': '#FF4500',  # 橙红色
        '晴冷': '#87CEEB',  # 天蓝色
        '晴朗': '#FFFF00',  # 黄色
        '雨天': '#1E90FF',  # 道奇蓝
        '小雨': '#6495ED',  # 玉米花蓝
        '中雨': '#4169E1',  # 皇家蓝
        '大雨': '#0000CD',  # 中蓝色
        '暴雨': '#00008B',  # 深蓝色
        '暴风雨': '#4B0082',  # 靛蓝色
        '阴天': '#A9A9A9',  # 暗灰色
        '阴冷': '#696969',  # 深灰色
        '下雪': '#F0FFFF',  # 雪白
        '大风': '#D3D3D3',  # 浅灰色
        '酷暑': '#FF0000',  # 红色
        '闷热': '#CD5C5C',  # 印度红
        '其他': '#808080'  # 灰色
    }

    # 按标签顺序获取颜色
    pie_colors = [colors.get(label, '#808080') for label in labels]

    fig, ax = plt.subplots(figsize=(12, 8))
    wedges, texts, autotexts = ax.pie(
        sizes, colors=pie_colors, autopct='%1.1f%%',
        startangle=140, textprops={'fontsize': 10},
        wedgeprops={'edgecolor': 'w', 'linewidth': 1}
    )

    # 添加图例（将图例放在右侧）
    ax.legend(wedges, labels, title="天气类型",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1),
              fontsize=12)

    ax.set_title(title, fontsize=16)
    ax.axis('equal')  # 保证饼图是圆的

    plt.tight_layout()
    plt.savefig('weather_pie_chart.png', dpi=300, bbox_inches='tight')
    print("饼状图已保存为 weather_pie_chart.png")


def plot_bar_chart(weather_classification, title="天气类型天数条形图"):
    """绘制带标签的条形图"""
    labels = list(weather_classification.keys())
    sizes = list(weather_classification.values())

    # 定义每种天气类型的颜色（与饼图保持一致）
    colors = {
        '晴天': '#FFD700',  # 金色
        '晴热': '#FF4500',  # 橙红色
        '晴冷': '#87CEEB',  # 天蓝色
        '晴朗': '#FFFF00',  # 黄色
        '雨天': '#1E90FF',  # 道奇蓝
        '小雨': '#6495ED',  # 玉米花蓝
        '中雨': '#4169E1',  # 皇家蓝
        '大雨': '#0000CD',  # 中蓝色
        '暴雨': '#00008B',  # 深蓝色
        '暴风雨': '#4B0082',  # 靛蓝色
        '阴天': '#A9A9A9',  # 暗灰色
        '阴冷': '#696969',  # 深灰色
        '下雪': '#F0FFFF',  # 雪白
        '大风': '#D3D3D3',  # 浅灰色
        '酷暑': '#FF0000',  # 红色
        '闷热': '#CD5C5C',  # 印度红
        '其他': '#808080'  # 灰色
    }

    # 按标签顺序获取颜色
    bar_colors = [colors.get(label, '#808080') for label in labels]

    fig, ax = plt.subplots(figsize=(14, 7))
    bars = ax.bar(labels, sizes, color=bar_colors)

    ax.set_xlabel('天气类型', fontsize=14)
    ax.set_ylabel('天数', fontsize=14)
    ax.set_title(title, fontsize=16)

    # 为每个条形添加数值标签
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., height + 0.5,
                f'{height}', ha='center', va='bottom', fontsize=12)

    # 旋转x轴标签避免重叠
    plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    plt.savefig('weather_bar_chart.png', dpi=300)
    print("条形图已保存为 weather_bar_chart.png")


def print_weather_table(weather_classification, start_date, end_date):
    """打印天气分类统计表"""
    print("\n" + "=" * 40)
    print(f"  {start_date} 至 {end_date} 天气分类统计表")
    print("=" * 40)
    print("天气类型\t天数\t占比")
    print("-" * 40)

    total_days = sum(weather_classification.values())
    for weather_type, count in sorted(
            weather_classification.items(),
            key=lambda x: x[1],
            reverse=True
    ):
        percentage = (count / total_days) * 100
        print(f"{weather_type}\t\t{count}\t{percentage:.1f}%")

    print("-" * 40)
    print(f"总计\t\t{total_days}\t100.0%")
    print("=" * 40 + "\n")


def get_valid_date(prompt):
    """获取用户输入的有效日期"""
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return date_str
        except ValueError:
            print("日期格式错误，请使用YYYY-MM-DD格式！")


def classify():
    filename = input("请输入数据文件名 (默认: seattle-weather.csv): ")
    if not filename.strip():
        filename = 'seattle-weather.csv'

    # 读取数据
    data = data_util.datatolist(filename)

    if not data:
        print(f"无法读取文件: {filename}")
        print("请检查文件路径和格式是否正确。")
        exit()

    # 检查数据列完整性
    headers = data[0]
    required_columns = ['date', 'weather']
    missing_columns = [col for col in required_columns if col not in headers]
    if missing_columns:
        print(f"错误：数据缺少必要的列: {', '.join(missing_columns)}")
        exit()

    # 获取用户输入的日期范围
    print("\n欢迎使用智能天气数据分析工具")
    print("=" * 40)

    choice = input("请选择分析模式 (1-指定日期范围, 2-全量数据): ")

    if choice == '1':
        start_date = get_valid_date("请输入开始日期 (YYYY-MM-DD): ")
        end_date = get_valid_date("请输入结束日期 (YYYY-MM-DD): ")

        # 验证日期顺序
        if datetime.strptime(start_date, '%Y-%m-%d') > datetime.strptime(end_date, '%Y-%m-%d'):
            print("错误：开始日期不能晚于结束日期！")
            exit()

        weather_class = classify_weather(data, start_date, end_date)
        title_suffix = f"({start_date}至{end_date})"
    else:
        weather_class = classify_weather(data)
        start_date = "全部"
        end_date = "数据"
        title_suffix = ""

    # 打印统计表格
    print_weather_table(weather_class, start_date, end_date)

    # 生成图表
    plot_pie_chart(weather_class, f"不同天气类型占比饼状图{title_suffix}")
    plot_bar_chart(weather_class, f"不同天气类型天数条形图{title_suffix}")

    print("数据处理和可视化完成！")
    
