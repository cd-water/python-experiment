from datatolist import datatolist
from datewash_gupiao import clean_data_list

if __name__ == '__main__':
    file_path = '002116.xlsx'
    data = datatolist(file_path)

    cleaned_data = clean_data_list(data)

    for row in cleaned_data[:6]:  
        print(row)
