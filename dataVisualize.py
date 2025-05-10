import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
mpg = sns.load_dataset('mpg')
tips = sns.load_dataset('tips')

air = pd.read_csv("air.csv")
print(air)


# air["station_london"].plot()
# air.plot.scatter(x="station_london", y="station_paris")
# air.plot.box()ۨ
# air.plot.area(figsize=(9,4), subplots=True)
plt.plot(air["station_london"],air["station_paris"], 'g^')
plt.show()



# print("\ntip data")
# print(tips)
# print("\niris data")


# #heatmaps:

# data = np.random.rand(5,5)
# print(data)
# print(data.shape)
# sns.heatmap(data,annot=True,cmap='coolwarm')
# plt.title("Heatmap Example")
# plt.show()


# # boxplot example

# sns.boxplot(x='day', y='total_bill', data=tips)
# plt.title("Boxplot of total bill by week days")
# plt.xlabel("No of week Days")
# plt.ylabel("Total bill ($):")
# plt.show()


# # pair plot example

# sns.pairplot(iris, hue='species')
# plt.suptitle("PairPlot Example", y=1.02)
# plt.tight_layout()
# plt.tight_layout()
# plt.show()


# # Distribution Plot:
# sns.histplot(tips['total_bill'], kde=True)
# plt.title("Distribution Plot with KDE:")
# plt.show()


# # Correlation:
# # select only numeric values from tips
# numeric_tips = tips.select_dtypes(include=['float64', 'int64'])
# correlation = numeric_tips.corr()

# sns.heatmap(correlation, annot=True, cmap='coolwarm')
# plt.title("Correlation Heatmap of Numeric Variables in Tips Dataset")
# plt.show()


# # plot aesthetic and customization
# # 1. First set style and palette
# sns.set_style('dark')
# sns.set_palette('pastel') #deep, muted, dark, colorblind

# sns.boxplot(x='day',  y='total_bill', data=tips)
# plt.title("Customize Boxplot")
# plt.show()

# # themes available: "darkgrid", "whitegrid", "dark", "white"

# # context adjustment: (talk, poster, paper, notebook)
# sns.set_context("poster")
# sns.scatterplot(x='day', y="total_bill", data=tips)
# plt.title("ScatterPlot with Poster Context")
# plt.show()

# # create Violin Plot
# sns.violinplot(x='day',y='total_bill', data=tips)
# plt.title("Violin plot of total bills of day")
# plt.xlabel("Days of the week")
# plt.ylabel("Total bill ($)")
# plt.show()


# # Create a swarmplot
# sns.swarmplot(x='day',y='total_bill', data=tips)
# plt.title("Swarm plot of total bills of day")
# plt.xlabel("Days of the week")
# plt.ylabel("Total bill ($)")
# plt.show()


# # barplot
# sns.barplot(x='day',y='total_bill', data=tips)
# plt.title("Bar plot of total bills of day")
# plt.xlabel("Days of the week")
# plt.ylabel("Total bill ($)")
# plt.show()

