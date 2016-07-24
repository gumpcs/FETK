#-*-coding:utf-8 -*-
"""
数据准备
"""
# Author:gump

import pandas as pd

def load_data(data_path = "../datasets/tianchi_fresh_comp_train_item.csv"):
    dataframe = pd.read_csv(data_path)
    return dataframe


# test code
if __name__ == '__main__':
    data_path = "../datasets/tianchi_fresh_comp_train_item.csv"
    dataframe = load_data()
    print dataframe


