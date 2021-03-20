# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:22:59 2020

@author: Jack Owen
"""


import matplotlib.pyplot as plt
import pandas as pd

file = pd.read_excel(r'C:\Users\Jack Owen\Documents\College\Research Project\Recievers.xlsx')
file2 = pd.read_excel(r'C:\Users\Jack Owen\Documents\College\Research Project\Running Backs.xlsx')

# "two" through "eleven" are no longer needed since we decided one pro bowl or more was success
zero = 0
one = 0
# two = 0
# three = 0
# four = 0
# five = 0
# six = 0
# seven = 0
# eight = 0
# nine = 0
# ten = 0
# eleven = 0

# instead of counting how many, only counting whether they made at least one 
for i in file.Pbowls:
    if i != 0:
        one += 1
    else:
        zero += 1
for i in file2.Pbowls:
    if i != 0:
        one += 1
    else:
        zero += 1

titles = ['Never Made a Pro Bowl', 'Made a Pro Bowl']
data = [zero, one]
explode = (0, 0.25)

plt.figure()
plt.title('Chance Of Making a Pro Bowl')
plt.pie(data, labels=titles, explode=explode, shadow=True, startangle=0, autopct='%1.1f%%')
plt.show()
