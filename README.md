# pands-project 2021

# Python –Using the Iris Dataset 


Python is a simple high-level and an open-source language used for general-purpose programming. For this project I will be demonstrating how to use python in practice when analysing data. I will be using Python 3 and a selection of libraries which provide different functions for data analysis and manipulation of the iris dataset. 

This article is written using Jupyter notebooks, which combines two components - A web application for interactive authoring and editing. The second component is notebooks documents, which can show all the content visible in the web application including inputs and outputs of the computations, explanatory text, mathematics, images, and rich media representations of objects.  

The Iris flower data set or Fishers data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis.This is perhaps the best known database to be found in the pattern recognition literature, and is frequently referenced to this day.
The iris data set gives the measurements in centimetres of the variables sepal length and width and petal length and width, respectively, for 50 flowers from each of 3 species of iris. The species are Iris setosa, versicolor, and virginica. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

The dataset contains a set of 150 records under 5 attributes:
1.	sepal length in cm
2.	sepal width in cm
3.	petal length in cm
4.	petal width in cm
5.	species:
-	Iris Versicolour
-	Iris Setosa
-	Iris Virginica


Several versions of the dataset have been published, the dataset being used in this project has been downloaded from - UCI Machine Learning Repository. 


# Libraries


```python
#Library Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

```


```python
#set plottimg styles of graphs using seaborn
sns.set()
```

## Pandas

Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008. 


## NumPy

NumPy is a python library used for working with arrays, it can process these arrays up to 50 times faster than traditional python lists and therefore is very useful in data science where arrays are frequently used and speed and resources are very important. 


## Matplotlib

Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
Matplotlib is open source and we can use it freely.
Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.


## Seaborn

Seaborn enables you to change the presentation of your plots by changing the style of elements like the background color, grids, and spines.Seaborn offers a lot of opportunities to customize your plots and have them show a distinct style. The color of your background, background style such as lines and ticks, and the size of your font all play a role in improving legibility and aesthetics.
Seaborn also allows you to style Matplotlib plots






# Dataset
Importing the Dataset _irdata_ using pandas, format dataset and test rows 0 - 9.


```python
#using pandas to read .data files
irdata =  pd.read_csv('iris.data', sep=",")

# Labelling the variables in the dataset
irdata.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

#testing the first 10 data sets print correctly
print(irdata.head (10))
```

       sepal_length  sepal_width  petal_length  petal_width      species
    0           4.9          3.0           1.4          0.2  Iris-setosa
    1           4.7          3.2           1.3          0.2  Iris-setosa
    2           4.6          3.1           1.5          0.2  Iris-setosa
    3           5.0          3.6           1.4          0.2  Iris-setosa
    4           5.4          3.9           1.7          0.4  Iris-setosa
    5           4.6          3.4           1.4          0.3  Iris-setosa
    6           5.0          3.4           1.5          0.2  Iris-setosa
    7           4.4          2.9           1.4          0.2  Iris-setosa
    8           4.9          3.1           1.5          0.1  Iris-setosa
    9           5.4          3.7           1.5          0.2  Iris-setosa
    

# Summary of the dataset



**info()**: provides a concise summary of a dataframe. It shows you all the information you need to know about your dataframe like: record counts, column names, data types, index range , and memory usage.


```python
irdata.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 149 entries, 0 to 148
    Data columns (total 5 columns):
     #   Column        Non-Null Count  Dtype  
    ---  ------        --------------  -----  
     0   sepal_length  149 non-null    float64
     1   sepal_width   149 non-null    float64
     2   petal_length  149 non-null    float64
     3   petal_width   149 non-null    float64
     4   species       149 non-null    object 
    dtypes: float64(4), object(1)
    memory usage: 5.9+ KB
    

**describe()**: from the pandas library provides a summary of the statistical data


```python
irdata.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>149.000000</td>
      <td>149.000000</td>
      <td>149.000000</td>
      <td>149.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>5.848322</td>
      <td>3.054362</td>
      <td>3.773826</td>
      <td>1.206040</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.828594</td>
      <td>0.435810</td>
      <td>1.760543</td>
      <td>0.760354</td>
    </tr>
    <tr>
      <th>min</th>
      <td>4.300000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.100000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>5.100000</td>
      <td>2.800000</td>
      <td>1.600000</td>
      <td>0.300000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>5.800000</td>
      <td>3.000000</td>
      <td>4.400000</td>
      <td>1.300000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>6.400000</td>
      <td>3.300000</td>
      <td>5.100000</td>
      <td>1.800000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.900000</td>
      <td>4.400000</td>
      <td>6.900000</td>
      <td>2.500000</td>
    </tr>
  </tbody>
</table>
</div>



## Creating text files of summary analysis of dataset, and summaries of each variable 


```python

#Summary of dataset
# to save a text file, open() returns a file object, 
# it is most commonly used with two arguments: open(filename, mode).
# 'w' is python write mode, this mode is used to edit and write new information
#f.write(string) writes the contents of string to the new file  
   
with open ("Summary.txt","w") as f:
 f.write ("\n")
 f.write ("Overview of the whole dataset:")
 f.write ("\n")
 f.write (str(irdata))
 f.write ("\n\n")
 f.write ("Basic Statistics")
 f.write (str(irdata.describe()))   
 f.write ("\n")
 

 

 f.close() 



```

Summary text file of Sepal Width


```python
#assign variable sepal width to sepal width array of data by using square brackets
sepal_width = irdata ['sepal_width']
#saving a text file of data as string 
with open ('sepal_width.txt', 'w') as f:
    f.write(str(sepal_width.describe()))
```

Summary text file of Sepal Length


```python
sepal_length = irdata ['sepal_length']
with open ('sepal_length.txt', 'w') as f:
    f.write(str(sepal_length.describe()))
```

Summary text file of Petal Length


```python
petal_length = irdata ['petal_length']
with open ('petal_length.txt', 'w') as f:
    f.write(str(petal_length.describe()))

```

Summary text file of Petal width


```python
petal_width = irdata ['petal_width']
with open ('petal_width.txt', 'w') as f:
    f.write(str(petal_width.describe()))
```


```python
#define the variable species
species = irdata ['species']

```

# Pandas DataFrames
DataFrames come with the pandas library, and are defined as two dimensional labeled data structures with columns of potentially different types. Using DataFrames to structure the data will help make it easier to manipulate the data and select columns needed to produce plots for the analysis of the Iris dataset. 


```python
#create dataframe and assign data
df = pd.DataFrame({ 'species': species, 'sepal_length': sepal_length, 'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width})
```

# Histograms
The below histograms help to show the distribution of features in the dataset, different colours have been used for each species this helps to show the variations. 


```python
#creating histogram plot using the DataFrame. 

#Seaborn hue is used to customise plot to include colours for the different species 
#kind - is set to present dataframe as histogram#kind - is set to present dataframe as histogram
sns.displot(data= df, x="sepal_length", hue="species", kind= "hist")

#adding title
plt.title("Sepal Length (cm)")

#saving histogram to png file
plt.savefig('sepal_length.png')



```


    
<img src = "https://github.com/susehenry/pands-project/blob/main/sepal_length.png" alt = "Sepal length" width = "450" height = "450"> 
    



```python

sns.displot(data= df, x="sepal_width", hue="species", kind= "hist")
plt.title("Sepal Width (cm)")
plt.savefig('sepal_width.png')
```


    
<img src = "https://github.com/susehenry/pands-project/blob/main/sepal_width.png" alt = "Sepal width" width = "450" height = "450"> 
    



```python

sns.displot(data= df, x="petal_length", hue="species", kind="hist")
plt.title("Petal Length (cm)")
plt.savefig('petal_length.png')

```


<img src = "https://github.com/susehenry/pands-project/blob/main/petal_length.png" alt = "Petal length" width = "450" height = "450">   

    



```python

sns.displot(data= df, x="petal_width", hue="species", kind= "hist")
plt.title("Petal Width (cm)")
plt.savefig('petal_width.png')

```


    
<img src = "https://github.com/susehenry/pands-project/blob/main/petal_width.png" alt = "Petal Width" width = "450" height = "450">
    


# Scatter plots of each pair of variables
This type of analysis allows you to compare two variables against each other to discern what kind of pattern if any is present. And what that pattern means


```python
# the same DataFrame is used to individually plot each pair of variables using seaborn scatterplots

# scatterplot to compare sepal length and width
sns.scatterplot (data=df, x= sepal_length, y = sepal_width, hue = "species")

#Adding a title
plt.title ("Sepal Length and Sepal Width comparison")

# Customising legend for the plot
plt.legend(bbox_to_anchor=(1, 1),
           borderaxespad=0)

plt.show()
           
```


    
![png](output_31_0.png)
    



```python
#scatter plot to compare petal length and width

sns.scatterplot (data=df, x= petal_length, y = petal_width, hue = "species")
plt.title ("Petal Length and Petal Width comparison")
plt.legend(bbox_to_anchor=(1, 1),
           borderaxespad=0)
plt.show()
```


    
![png](output_32_0.png)
    


# # Seaborn - PairGrid
Another way to code plots in python is to use the constructor PairGrid, this enables you to draw a grid of subplots that plot pairwise relationships in a data set using the same plot type (e.g. scatterplots) to visualize the data.


```python
#initialise PairGrid using same dataframe (df) as before
pair = sns.PairGrid (df, hue="species")

# PairGrid.map() will draw a bivariate plot on every axes
#type of plot - scatterplot
pair.map (sns.scatterplot)

#adding a legend
pair.add_legend ()

plt.show()
```


    
![png](output_34_0.png)
    


There are lots of other various types of plots in the Seaborn library that can be created to help in the analysis of the dataset examples of these are -
- sns.pairplot
- sns.violinplot
- sns.boxplot
- sns.Implot
- sns.barplot




# Concluson

The histograms give us a basic visual for the main distribution of features for each species and show there is a difference between the iris setosa petal length and petal width compared to the two other species of Iris. The scatterplots help to further show the relationships between the variables in the three different iris species. The above scatterplots do show differences in the variables in the Iris setosa compared to the other species, the Iris setosa can be seen to have its own cluster in each of the scatterplots this makes it easy to determine the Iris setosa species by its measurements in sepal length, sepal width, petal length and petal width and tell it apart from the other two Iris species. There is some overlap in the variables measured for the Iris-veriscolour and Iris-virginica you can see this in the scatterplots as the clusters are not clearly defined and are harder to differentiate, further analysing and modelling of the data would be required. 

# References


**Python**


https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/ 

**Jupyter**


https://jupyter-notebook.readthedocs.io/en/latest/notebook.html 

https://jupyter.readthedocs.io/en/latest/index.html

**Iris Data Set**


https://en.wikipedia.org/wiki/Iris_flower_data_set

UCI Machine Learning Repository: Iris Data Set http://archive.ics.uci.edu/ml/datasets/Iris/ 

**Pandas**


https://www.w3schools.com/python/pandas/pandas_intro.asp 

**NumPy**


Introduction to NumPy (w3schools.com)
https://www.w3schools.com/python/numpy/numpy_intro.asp


**Data Analysis**


Intro to Machine Learning with Python 2: Exploratory Data Analysis - YouTube
https://www.youtube.com/watch?v=6BagRiSY1ds&list=PLMAyPTgGwv2DUV6DZib9eMetsTTX87JNr&index=2



**Matplotlib**

https://www.w3schools.com/python/matplotlib_intro.asp 


**Reading and writing files**

Input and Output — Python 2.7.18 documentation https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files


**Summarising Data**

How to Summarize Data with Pandas, Python - Datapott Analytics 
https://datapott.com/how-to-summarize-data-with-pandas-python/

**DataFrames**

Pandas Tutorial: DataFrames in Python - DataCamp
https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python

**Histograms**

seaborn.histplot — seaborn 0.11.1 documentation (pydata.org) https://seaborn.pydata.org/generated/seaborn.histplot.html

Seaborn Histogram using sns.distplot() - Python Seaborn Tutorial (indianaiproduction.com)
https://indianaiproduction.com/seaborn-histogram-using-seaborn-distplot/

