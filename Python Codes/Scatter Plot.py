# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:54:02 2020

@author: Jack Owen
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_excel(r'C:\Users\Jack Owen\Documents\College\Research Project\Pro Bowl Recievers.xlsx')

# the original intent was for this to print out the graph for both recievers and running backs
# it was easier to read seperately though
file2 = pd.read_excel(r'C:\Users\Jack Owen\Documents\College\Research Project\Pro Bowl Running Backs.xlsx')

measure1=file.dropna(subset=['Wt'])

# can change "file" to "file2" to swap faster
# also "Wt" can be changed to whichever measurement you'd like to compare against # of pro bowls
x = file.Wt.dropna(how='any')

y = measure1.Pbowls  # need to drop any missing categories


print(x.size)
print(y.size)


plt.figure()
plt.scatter(x, y)
plt.ylabel('# of Pro Bowls')
plt.xlabel('Weight (WR)')

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), 'r--')

plt.show()
