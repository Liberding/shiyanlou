# -*- coding:utf-8 -*-

import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    s = pd.Series(data['Volume'].values, index=(pd.to_datetime(data['Date'])))
    second_volume = s.resample('Q').sum().sort_values()[-2]
    return second_volume

if __name__ == '__main__':
    quarter_volume()
