import re
from datetime import datetime

# 日期校验函数
def is_valid_date(date_str):
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

# 数据清洗函数
def clean_data_list(data_list):
    if not data_list:
        raise ValueError("数据为空，无法清洗")
        
    headers = data_list[0]
    rows = data_list[1:]

    try:
        date_idx = headers.index('日期')
        open_idx = headers.index('开盘')
        close_idx = headers.index('收盘')
        change_idx = headers.index('涨跌额')
    except ValueError as e:
        raise KeyError(f"列缺失: {e}")

    cleaned_rows = []
    for row in rows:
        date_str = str(row[date_idx]).strip().replace('/', '-').replace('.', '-')
        if not is_valid_date(date_str):
            continue
        row[date_idx] = date_str

        try:
            open_price = float(row[open_idx])
            close_price = float(row[close_idx])
            row[change_idx] = round(close_price - open_price, 2)
        except:
            continue

        cleaned_rows.append(row)

    return [headers] + cleaned_rows
