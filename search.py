import sys
import pandas as pd
import numpy as np
import pandas_datareader as pdr
from datetime import datetime


class Symbol:
    def __init__(self, symbol):
        self.symbol = symbol
        self.search_symbol()

    def search_symbol(self):
        data = pdr.get_data_stooq(symbols=self.symbol, start=datetime(2000, 1, 1), end=datetime.now())
        # print(data)
        ans = self.calculate(data)
        # get competitor (market share +=
        # show graph
        print('standard deviation for ' + self.symbol + ' is: ', round(ans, 5))
        # new_table = amd_data.assign(Return=amd_data.get('Adj Close') - amd_data.get('Open'))
        # print(new_table)
        # r_bar = new_table.get('Return').sum() / new_table.shape[0]
        # print('R Bar value is', round(r_bar, 5))
        # top = 0
        # for i in range(new_table.shape[0]):
        # a = (new_table.get('Return').iloc[i] - r_bar) ** 2
        # top = a + top
        # std = np.sqrt(top / ((new_table.shape[0]) - 1))
        # print('standard deviation is', round(std, 5))

    @staticmethod
    def calculate(data):
        new_table = data.assign(Return=data.get('Close') - data.get('Open'))
        print(new_table)
        r_bar = new_table.get('Return').sum() / new_table.shape[0]
        top = 0
        for i in range(len(new_table)):
            a = (new_table.get('Return').iloc[i] - r_bar) ** 2
            top = a + top
        std = np.sqrt(top / ((new_table.shape[0]) - 1))
        return std
