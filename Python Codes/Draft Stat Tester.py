# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:41:07 2020

@author: Jack Owen
"""


# Import necessary packages first
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# '%matplotlib inline' for jupyter notebook


# read excel file
Recievers = pd.read_excel(r'C:\Users\Jack Owen\Documents\College\Research Project\Recievers.xlsx')
PBRecievers = pd.read_excel(r'C:\Users\Jack Owen\Documents\College\Research Project\Pro Bowl Recievers.xlsx')
RBacks = pd.read_excel(r'C:\Users\Jack Owen\Documents\College\Research Project\Running Backs.xlsx')
PBRBacks = pd.read_excel(r'C:\Users\Jack Owen\Documents\College\Research Project\Pro Bowl Running Backs.xlsx')


# display numerical data for files
print('\n Pro Bowl Running Back Details')
print(PBRBacks.describe())
print('\n Running Back Details')
print(RBacks.describe())
print('\n Pro Bowl Recievers Details')
print(PBRecievers.describe())
print("\n Wide Reciever Details")
print(Recievers.describe())


# Set our variables for boxplot measurements
Weight = [Recievers.Wt.dropna(), PBRecievers.Wt.dropna(),
          RBacks.Wt.dropna(), PBRBacks.Wt.dropna()]

Forty = [Recievers.Forty.dropna(), PBRecievers.Forty.dropna(),
         RBacks.Forty.dropna(), PBRBacks.Forty.dropna()]

Vertical = [Recievers.Vertical.dropna(), PBRecievers.Vertical.dropna(),
            RBacks.Vertical.dropna(), PBRBacks.Vertical.dropna()]

Bench = [Recievers.BenchReps.dropna(), PBRecievers.BenchReps.dropna(),
         RBacks.BenchReps.dropna(), PBRBacks.BenchReps.dropna()]

Broad = [Recievers.BroadJump.dropna(), PBRecievers.BroadJump.dropna(),
         RBacks.BroadJump.dropna(), PBRBacks.BroadJump.dropna()]

Cone = [Recievers.Cone.dropna(), PBRecievers.Cone.dropna(),
        RBacks.Cone.dropna(), PBRBacks.Cone.dropna()]

Shuttle = [Recievers.Shuttle.dropna(), PBRecievers.Shuttle.dropna(),
           RBacks.Shuttle.dropna(), PBRBacks.Shuttle.dropna()]


# boxplot for each measurement to illustrate trends
fig = plt.figure()
ax = fig.add_subplot(111)

bp = ax.boxplot(Shuttle, patch_artist=True, vert=0)
colors = ['#2b83ba', '#abdda4', '#fdae61', '#d7191c']

for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

plt.title('20 YD Shuttle')
#plt.boxplot(Weight, vert=False)


# boxplot colors


# to create a legend in our boxplot
plt.plot([], c='#d7191c', label=('Pro Bowl Running Backs'))
plt.plot([], c='#fdae61', label='Running Backs')
plt.plot([], c='#abdda4', label='Pro Bowl Recievers')
plt.plot([], c='#2b83ba', label='Recievers')
plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")

# labels for axes
plt.yticks(range(1, 5), ' ')
plt.xlabel('Seconds')

# plt.tight_layout()
plt.show()
