import math
import re
from datetime import datetime


def is_valid_date_regex(date_str):
    # 匹配YYYY-MM-DD、YYYY/MM/DD、YYYY.MM.DD等格式
    pattern = r'^\d{4}[-/.]\d{2}[-/.]\d{2}$'
    if not re.match(pattern, date_str):
        return False

    # 进一步验证日期有效性
    try:
        separator = re.search(r'[-/.]', date_str).group()
        datetime.strptime(date_str, f"%Y{separator}%m{separator}%d")
        return True
    except (ValueError, AttributeError):
        return False


def weather_clean_MainCode(datalist, start_time, end_time):
    # 根据给的起始时间和终止时间，将原来的数据列表切片
    for x in datalist:
        if x[0] == start_time:
            start_index = datalist.index(x)
        if x[0] == end_time:
            end_index = datalist.index(x)
    datalist = datalist[start_index:end_index + 1]

    for x in datalist:
        if not is_valid_date_regex(x[0]):
            datalist.remove(x)
        else:
            datalist[datalist.index(x)][0] = re.sub(r'[-/.]', '-', x[0])
    return datalist


def weather_clean_data(datalist, index):
    count = 0
    sum = 0
    for x in datalist:
        if not math.isnan(float(x[index])):
            count += 1
            sum += float(x[index])
    avg = sum / count
    for x in datalist:
        if math.isnan(float(x[index])):
            datalist[datalist.index(x)][index] = str(avg)  # 将缺失的数据换为数据的平均值
    return datalist
