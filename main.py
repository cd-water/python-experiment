from datatolist import datatolist
from datewash_gupiao import clean_data_list

if __name__ == '__main__':
    file_path = '002116.xlsx'
    data = datatolist(file_path)

    cleaned_data, missing_data = clean_data_list(data)

    # 打印清洗后的数据（前6行）
    print("清洗后的数据：")
    for row in cleaned_data[:6]:
        print(row)

    # 打印缺失数据的行
    print("\n缺失数据的行：")
    for row in missing_data:
        print(row)
