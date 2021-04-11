# Analysis of Iris Data Set
# outputs a summary of each variable to a single text file, 
# saves a histogram of each variable to png files, and 
# outputs a scatter plot of each pair of variables. 




import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sns

sns.set()
#this function allows you the ability to use Seaborn default colors, 
# and Seaborn’s other styling techniques.

#using pandas to read .data files
irdata =  pd.read_csv('iris.data', sep=",")

# setting the variables in the dataset
irdata.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

#test first 10 data sets print
print(irdata.head (10))





