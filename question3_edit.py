# -*- coding: utf-8 -*-
"""Question3_Edit.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1elFfnKGnKxyJs7HtPEZGjo1dFCO7WYv-
"""

# This is a Python 3 file that generates data for
# prospective data engineer candidates.

import pandas as pd
from random import random
nums = list()

for i in range(0,10000):
    ui = 0;
    for x in range(0,12):
        ui = ui + random()
    nums.append(5 + 3*ui)
        
df = pd.DataFrame(nums)
df.to_csv("data.csv", header=0)
print("done.")

# Commented out IPython magic to ensure Python compatibility.
# Hmmm...  I wonder what this does?
import statistics
from matplotlib import pyplot as plt
# %matplotlib inline

plt.hist(nums, bins=100, range=[0,50])
print("Mean: {}".format(statistics.mean(nums)))
print("Std:  {}".format(statistics.stdev(nums)))

"""
1. Talking about the descriptive statistics in regards to the data that was provided above. First off let us define what a descriptive statistic is; A general definition for the term descriptive statics could be the following: A summary statistic that summarizes (quantitatively) features in regards to the collection of information. A descriptive Statistic is essentially a means of analysing our data collection.

Given:

1. Histogram: In general this shows the approximate distribution of our numerical data set. (A means of graphical representation).

2. Mean: The average of our data set (can be found by adding up all data points and dividing this value by the number of values in our set).

3. Standard Deviation(std): This is a measure of variation/dispersion in the given data set.


Thoughts (just looking at the data given):
1. We have an average value of 23.028 (Based off of the csv given this is for arbitrary data)

2. Based on a standard deviation value of 3 we have a decent spread in the data that was collected and synthesized. 99.7% of our data lies within 3 standard deviations of our mean(23.028). This could mean we have 99.7% confidence that would depend on the threshold of the project. (near certainty and certainty depend on the contrants of the project). EX: In certain fields of science only 2 standard deviations away from the mean are considered statistically significant. (just depends)

3. Just from looking at this histogram I don't see many outliers that show up visually. It might be smart to create a python script in-order to find the number of outliers that occur outside of a given range.

4. All and all from the data.csv looks like it has a solid distribution.

Final Thoughts:

Probably need more Quantitative figures + actual understanding of the data set to make further claims.
links: link text https://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule
"""