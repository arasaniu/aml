import numpy as np
import pandas

data_abdomen1 = []
data_abdomen2 = []
data_abdomen3 = []
data_thorax1 = []
data_thorax2 = []

def load_data():
    data_abdomen1 = pandas.read_csv('../data/abdomen1.txt')
    data_abdomen2 = pandas.read_csv('../data/abdomen2.txt')
    data_abdomen3 = pandas.read_csv('../data/abdomen3.txt')
    data_thorax1 = pandas.read_csv('../data/thorax1.txt')
    data_thorax2 = pandas.read_csv('../data/thorax2.txt')

    return data_abdomen1, data_abdomen2, data_abdomen3, data_thorax1, data_thorax2