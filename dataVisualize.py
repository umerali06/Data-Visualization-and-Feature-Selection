import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
mpg = sns.load_dataset('mpg')

tips = sns.load_dataset('tips')
print(tips)

air = pd.read_csv("air.csv")
print(air)


air["station_london"].plot() # plot mean ----> line bar
air.plot.scatter(x="station_london", y="station_paris")
air.plot.box()
air.plot.area(figsize=(9,4), subplots=True)
plt.plot(air["station_london"],air["station_paris"], 'g^') # where g mean grean color and ^ sign showing triangle type green line bar showing , we can use g-- which shows us green lines instead of triangles, -- we also can use 'go' which showing green circles to us same like r* --> red colr stars
plt.show() # use at the end always to display the diagrams


plt.plot([1,5,10,51],[23,40,33,60],'r--')
plt.scatter(air["station_london"],air["station_paris"]) # we also can write it as plt.scatter(x="station_london",y="station_paris", data=air) ---> this is quite better way to display 
plt.hist(air["station_paris"], density=True, facecolor="g") # in histogram only one cloumn we use , which in other plots we use 2 cloumns sets as x and y . histogram use bins=5 etc also ----> bins main intervals 1-20, 21-40, 41-60 etc how much we want, for this use bin
plt.xlabel("This is x label") # optional to use
plt.ylabel("This is Y label") # optional
plt.suptitle("This is our title") # suplot is the main whole image title , not the sub small image title
plt.show()

# in histogram --> one column use, can use bins=5 etc for intervals, can use kde (kernal density) this is optional , which is only use for styling 

#important qustion related the subplot.
groups = ["group1","group2","group3"]
values = [5,50,100]
plt.figure(figsize=(9,4))
plt.subplot(131)
plt.bar(groups, values)
plt.subplot(132)
plt.hist(groups, values)
plt.subplot(133)
plt.plot(values,groups)
plt.show()

#subplot second method:
fig, axs = plt.subplots(2,3, figsize=(9,3))
axs[0,0].bar(groups,values,color="purple")
axs[0,0].set_title("Bar Chart")

axs[0,1].hist(values)
axs[0,1].set_title("Histogram")

axs[0,2].plot(groups,values,"g--")
axs[0,2].set_title("Line Charts")

axs[1,0].bar(groups, values, color="yellow")
axs[1,0].set_title("Bar chart")

axs[1,1].scatter(groups,values)
axs[1,1].set_title("Scatter chart")

axs[1,2].plot(values, groups)
axs[1,2].set_title("Plot Chart")

plt.tight_layout() # force the subplots image to be use in the image layout
plt.show()




print("\ntip data")
print(tips)
print("\niris data")


#heatmaps:

data = np.random.rand(5,5)
print(data)
print(data.shape)
sns.heatmap(data,annot=True,cmap='coolwarm') # annot is use for the value on the color , if annot is false , numeric value is not showing , only color show -> if want numbers value on the plot then use annot in the heatmap. cmap is the color map -> coolwarn make two color for us , red for negative numbers and blue for positive numbers 
plt.title("Heatmap Example")
plt.show()


# # boxplot example

sns.boxplot(x='day', y='total_bill', data=tips) # same method use for all other plots
plt.title("Boxplot of total bill by week days")
plt.xlabel("No of week Days")
plt.ylabel("Total bill ($):")
plt.show()


# # pair plot example

sns.pairplot(iris, hue='species') # hue is optional , just use for the styling 
plt.suptitle("PairPlot Example", y=1.02) # where y is optional , it work is only to make little gap and make the title little above
plt.tight_layout()
plt.tight_layout()
plt.show()


# Distribution Plot:
sns.histplot(tips['total_bill'], kde=True) # kde (kernal denisty) optional use, use for the aesthetic look
plt.title("Distribution Plot with KDE:")
plt.show()

#important question:
# Correlation: --> for correlation we need numeric value , not string  value , so first filter numeric value
# select only numeric values from tips
numeric_tips = tips.select_dtypes(include=['float64', 'int64'])
correlation = numeric_tips.corr()

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Numeric Variables in Tips Dataset")
plt.show()


#optional things use for styling of the plots
# plot aesthetic and customization
# 1. First set style and palette
sns.set_style('dark')
sns.set_palette('pastel') #deep, muted, dark, colorblind

sns.boxplot(x='day',  y='total_bill', data=tips)
plt.title("Customize Boxplot")
plt.show()

# themes available: "darkgrid", "whitegrid", "dark", "white"

# context adjustment: (talk, poster, paper, notebook)
sns.set_context("poster")
sns.scatterplot(x='day', y="total_bill", data=tips)
plt.title("ScatterPlot with Poster Context")
plt.show()

# create Violin Plot
sns.violinplot(x='day',y='total_bill', data=tips)
plt.title("Violin plot of total bills of day")
plt.xlabel("Days of the week")
plt.ylabel("Total bill ($)")
plt.show()


# Create a swarmplot
sns.swarmplot(x='day',y='total_bill', data=tips)
plt.title("Swarm plot of total bills of day")
plt.xlabel("Days of the week")
plt.ylabel("Total bill ($)")
plt.show()


# barplot
sns.barplot(x='day',y='total_bill', data=tips)
plt.title("Bar plot of total bills of day")
plt.xlabel("Days of the week")
plt.ylabel("Total bill ($)")
plt.show()

