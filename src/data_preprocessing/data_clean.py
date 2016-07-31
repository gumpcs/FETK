#-*-coding:utf-8 -*-
"""
数据清洗模块
"""
# Author:gump

from scipy.stats import mode
import data_prepare

class DealWithMissingValues():
    """
    处理缺失值
    train_data: 需要清洗的数据，一般来自data_prepare模块
    """

    def __init__(self, data):
        self.data = data

    def simple_approaches_to_missing_data(self, strategy):
        """
        一些简单的基于统计学的处理缺失值数据的方法：均值填充，中位数填充，众数填充
        :return:
        """
        strategy = ['mean','median','most_frequent']

        # 找出含有缺失值的列
        missing_values_list = []
        attribution_counts_dict = dict(self.data)
        for attribution,counts in attribution_counts_dict.items():
            if counts < 2760:
                missing_values_list.append(attribution)

        # 如果是Nominal attribution，则可以使用‘most_frequent’
        # 这里缺失值只涉及到Nominal attribution
        self.nominal_attribution_list = missing_values_list
        # 如果是Numerical attribution,则可以使用'mean'
        #self.numerical_attribution_list = []


class DealWithNoisyData():
    """
    异常值处理
    """
    def __init__(self, data):
        self.data = data



# test code

if __name__ == '__main__':
    dataframe = data_prepare.load_data(data_path = '../datasets/tianchi_fresh_comp_train_item.csv')
    deal_with_missing_values_obj = DealWithMissingValues(dataframe)