import re
from datetime import datetime

# 日期校验函数
def is_valid_date(date_str):
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
    rows_with_missing_data = []  
    
    for row in rows:
        # 检查是否缺失数据,如果缺失则保存该行
        if not row[date_idx] or not row[open_idx] or not row[close_idx]:
            rows_with_missing_data.append(row)  
            continue  
        
        # 处理日期格式
        date_str = str(row[date_idx]).strip().replace('/', '-').replace('.', '-')
        if not is_valid_date(date_str):
            continue
        row[date_idx] = date_str

        try:
            open_price = float(row[open_idx])
            close_price = float(row[close_idx])
            row[change_idx] = round(close_price - open_price, 2)
        except:
            continue  # 如果有任何异常，跳过这行数据

        cleaned_rows.append(row)

    return [headers] + cleaned_rows, rows_with_missing_data
