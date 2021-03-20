# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:24:10 2020

@author: Jack Owen
"""

# handle NaN data in pandas example

import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.tail())

print(ufo.isnull().tail())

print(ufo.notnull().tail())

print(ufo.isnull().sum())  # sum(axis=0) makes it a column instead of row

print(pd.Series([True, False, True]).sum())  # makes true = 1, false = 2

print(ufo[ufo.City.isnull()])  # only prints data for cities that are null (25 cities)"""

print(ufo.shape)  # gives the shape of the file. 18241 rows X 5 columns

print(ufo.dropna(how='any').shape)  # temporarily drop a row if it has ANY missing data in it
# it won't change our original data, only uses data that we specified. super useful
# 'how='all'' drops value that has ALL missing value

print(ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape)
# drops data with any missing value in city or shape reported.
# could make it 'all' to make it both values have to be missing to be dropped