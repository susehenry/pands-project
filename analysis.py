# Analysis of Iris Data Set
# outputs a summary of each variable to a single text file, 
# saves a histogram of each variable to png files, and 
# outputs a scatter plot of each pair of variables. 

# author: Susan Henry




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
#this function allows you the ability to use Seaborn default colors, 
# and Seaborn’s other styling techniques.

#using pandas to read .data files
irdata =  pd.read_csv('iris.data', sep=",")

# labelling the variables in the dataset
irdata.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

#testing first 10 data sets to print
print(irdata.head (10))


#info(): provides a concise summary of a dataframe
irdata.info()

# describe() provides summary of statistical data
irdata.describe()

#to create a text summary of dataset

# open() returns a file object, 
# and is most commonly used with two arguments: open(filename, mode).
# 'w' is python write mode, this mode is used to edit and write new information
#f.write(string) writes the contents of string to the file  
 
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


#Summary text file sepal width
sepal_width = irdata ['sepal_width']
with open ('sepal_width.txt', 'w') as f:
    f.write(str(sepal_width.describe()))  

#Summary text file sepal length
sepal_length = irdata ['sepal_length']
with open ('sepal_length.txt', 'w') as f:
    f.write(str(sepal_length.describe()))

#Summary text file petal length
petal_length = irdata ['petal_length']
with open ('petal_length.txt', 'w') as f:
    f.write(str(petal_length.describe())) 

#Summary text file petal width
petal_width = irdata ['petal_width']
with open ('petal_width.txt', 'w') as f:
    f.write(str(petal_width.describe()))


#define the variable species
species = irdata ['species']


#create dataframe
df = pd.DataFrame({'species': species, 'sepal_length': sepal_length, 'sepal_width': sepal_width, 'petal_length': petal_length, 'petal_width': petal_width})

#Histograms
#histogram created using seaborn 

#sepal length histogram
#Seaborn hue is used to customise plot to include colours for the different species 
#kind - is set to present dataframe as histogram
sns.displot(data= df, x="sepal_length", hue="species", kind= "hist")
#adding a title
plt.title("Sepal Length (cm)")
#saving copy of histogram to png file
plt.savefig('sepal_length.png')


#sepal width histogram
sns.displot(data= df, x="sepal_width", hue="species", kind= "hist")
plt.title("Sepal Width (cm)")

#petal length histogram
sns.displot(data= df, x="petal_length", hue="species", kind="hist")
plt.title("Petal Length (cm)")

#petal width histogram
sns.displot(data= df, x="petal_width", hue="species", kind= "hist")
plt.title("Petal Width (cm)")




#scatter plots

# the same DataFrame is used to individually plot each pair of variables using seaborn scatterplots

# scatterplot to compare sepal length and width
sns.scatterplot (data=df, x= sepal_length, y = sepal_width, hue = "species")

#Adding a title
plt.title ("Sepal Length and Sepal Width comparison")

# Customising legend for the plot
plt.legend(bbox_to_anchor=(1, 1),
           borderaxespad=0)

plt.show()


#scatter plot to compare petal length and width

sns.scatterplot (data=df, x= petal_length, y = petal_width, hue = "species")
plt.title ("Petal Length and Petal Width comparison")
plt.legend(bbox_to_anchor=(1, 1),
           borderaxespad=0)
plt.show()


#PairGrid

#initialise PairGrid using same dataframe (df) as before
pair = sns.PairGrid (df, hue="species")

# PairGrid.map() will draw a bivariate plot on every axes
#type of plot - scatterplot
pair.map (sns.scatterplot)

#adding a legend
pair.add_legend ()

plt.show()







   




