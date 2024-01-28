import pandas as pd
import os

from src.Validators import validate_case, validate_type


def read_and_clean_excel(file):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')

    # File paths
    file_path1 = os.path.join(data_dir, 'datatF.2.xls')
    file_path2 = os.path.join(data_dir, 'datatest2.xls')
    file_path3 = os.path.join(data_dir, 'Random_data.xlsx')
    file_path4 = os.path.join(data_dir, 'big_Random_data.xlsx')
    file_path5 = os.path.join(data_dir, 'very_big_Random_data.xlsx')
    if file == 1:
        data = pd.read_excel(file_path1)[['time', 'dice11', 'dice12', 'dice13', 'total1', 'result', 'DiceR']][::-1]
    elif file == 3:
        data = pd.read_excel(file_path3)[['time', 'dice11', 'dice12', 'dice13', 'total1', 'result', 'DiceR']][::-1]
    elif file == 4:
        data = pd.read_excel(file_path4)[['time', 'dice11', 'dice12', 'dice13', 'total1', 'result']][::-1]
    elif file == 5:
        data = pd.read_excel(file_path5)[['time', 'dice11', 'dice12', 'dice13', 'total1', 'result']][::-1]

    else:
        data = pd.read_excel(file_path2)[['time', 'dice11', 'dice12', 'dice13', 'total1', 'result']][::-1]

    data['case'] = data.apply(
        lambda row: validate_case(row['total1'], row['dice11'], row['dice12'], row['dice13']).value,
        axis=1)
    data['type'] = data.apply(lambda row: validate_type(row['total1']).value, axis=1)
    data['DiceF1'] = data.apply(lambda row: f"{row['dice11']}-{row['dice12']}-{row['dice13']}", axis=1)
    data['DiceR'] = data['DiceF1'].shift(-1).fillna("1-3-4").astype(str)
    return data
