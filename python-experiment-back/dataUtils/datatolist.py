import pandas as pd


def csvtolist(filename):
    df = pd.read_csv(filename)
    c_list = [df.columns.tolist()] + df.values.tolist()
    return c_list

def exceltolist(filename):
    df = pd.read_excel(filename)
    c_list = [df.columns.tolist()] + df.values.tolist()
    return c_list

def datatolist(filename):
    index = filename.rfind('.')
    type = filename[index+1:]
    if type == 'csv':
        return csvtolist(filename)
    elif type == 'excel':
        return exceltolist(filename)
    else:
        return []