import math
import re
from datetime import datetime
import pandas as pd

def is_valid_date_regex(date_str):
    """检查日期格式是否为YYYY-MM-DD、YYYY/MM/DD、YYYY.MM.DD,且逻辑上合法"""
    pattern = r'^\d{4}[-/.]\d{2}[-/.]\d{2}$'
    if not re.match(pattern, date_str):
        return False
    try:
        sep = re.search(r'[-/.]', date_str).group()
        datetime.strptime(date_str, f"%Y{sep}%m{sep}%d")
        return True
    except:
        return False  

def fahrenheit_to_celsius(fahrenheit):
    """将华氏度转换为摄氏度"""
    return (fahrenheit - 32) * 5 / 9

def is_valid_wind_speed(wind_speed):
    """检查风速是否在有效范围 0-16级之间"""
    try:
        wind_speed = float(wind_speed)
        return 0 <= wind_speed <= 16
    except ValueError:
        return False

def weather_clean_MainCode(datalist, start_time, end_time):
    """根据起止时间切片数据，并清洗日期格式，去除非法日期"""
    # 找起止索引
    start_index, end_index = None, None
    for i, row in enumerate(datalist):
        if row[0] == start_time:
            start_index = i
        if row[0] == end_time:
            end_index = i

    if start_index is None or end_index is None or start_index > end_index:
        print("时间区间无效")
        return []

    sliced = datalist[start_index:end_index + 1]

    cleaned = []
    for row in sliced:
        date_str = row[0]
        if is_valid_date_regex(date_str):
            # 格式化为统一 YYYY-MM-DD
            standard_date = re.sub(r'[-/.]', '-', date_str)
            new_row = row.copy()
            new_row[0] = standard_date
            cleaned.append(new_row)
        else:
            print(f"跳过非法日期：{date_str}")
    return cleaned



def weather_clean_data(datalist, index, temp_unit_index=None, wind_speed_index=None):
    """将指定列中的 NaN 或空值替换为该列的平均值，并做温度转换和风速校验"""
    values = []

    #计算平均值
    for row in datalist[1:]: 
        try:
            val = float(row[index])
            if not math.isnan(val):
                values.append(val)
        except:
            continue

    if not values:
        print("列中无有效数据，无法计算平均值")
        return datalist

    avg = sum(values) / len(values)

    for i in range(1, len(datalist)):
        try:
            val = float(datalist[i][index])
            if math.isnan(val):
                datalist[i][index] = avg
        except:
            datalist[i][index] = avg

        # 温度转换
        if temp_unit_index is not None and len(datalist[i]) > temp_unit_index:
            temp_value = datalist[i][temp_unit_index]
            if isinstance(temp_value, (float, int)): 
                if temp_value > 50:  # 假设温度大于50是华氏度
                    celsius = fahrenheit_to_celsius(temp_value)
                    datalist[i][temp_unit_index] = round(celsius, 2)

        # 风速校验
        if wind_speed_index is not None and len(datalist[i]) > wind_speed_index:
            wind_value = datalist[i][wind_speed_index]
            if not is_valid_wind_speed(wind_value):
                datalist[i][wind_speed_index] = avg  # 风速无效用平均风速替代

    return datalist
