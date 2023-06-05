# Seaborn - Visualization Library which is built on matplotlib So import matplotlib also

import seaborn as sns
from matplotlib import pyplot as plt 
print(sns.__version__) # To check the version of seaborn library


# # Inside seaborn there are built-in dataset and one of them is fmri dataset 
# #  A dataset that contains functional magnetic resonance imaging (fMRI) data, used for studying brain activity. It includes information about different brain regions and their response to various stimuli.
# # It has load_ dataset method
# print("\fmri Dataset\n")
# fmri = sns.load_dataset("fmri")
# print(fmri.head())
# print(fmri.describe())

# # Other datasets which seaborn library conntains
# print("Titanic Dataset")
# titanic=sns.load_dataset("titanic")
# print(titanic.describe())
# print(titanic.head())

print("\nTips Dataset\n")
tips=sns.load_dataset("tips")
print(tips.describe())
print(tips.head())

print("\nDiamonds Dataset\n")
diamonds=sns.load_dataset("diamonds")
print(diamonds.describe())
print(diamonds.head())

print("\Iris Dataset\n")
iris=sns.load_dataset("iris")
print(iris.describe())
print(iris.head())

# dataset_names = sns.get_dataset_names()
# for name in dataset_names:
#     data = sns.load_dataset(name)
#     print(f"Dataset: {name}")
#     print(data.head())
#     print("--------------------------------------------------\n")


# # Line Plot 
# sns.lineplot(x="timepoint",y="signal",data=fmri,hue="event") #New attribute - We are mapping the event columns onto hue attribute and color of the line will be dependent on the event column 
# # we can map a column onto the hue asthetics
# # sns.lineplot(x="timepoint",y="signal",data=fmri) only prints the blue line curve 
# plt.show()

# # Styles snd marker of Line plot 
# sns.lineplot(x="timepoint",y="signal",data=fmri,hue="event",style="event",marker=True)
# plt.show()

# # Creating barplot on seaborn dataset
# sns.set(style="whitegrid")
# sns.barplot(x="pclass",y="survived",data=titanic) # make sure you enter column name proplerly since python is case-sensitive
# plt.show()

# # SeaBorn Bar Plot 2
# sns.barplot(x="pclass",y="age",hue="sibsp",data=titanic) # Color will be determined by the sibsp hue attribute
# plt.show()

# # Different palettes 
# sns.barplot(x="pclass",y="survived",data=titanic,palette='Blues_d')
# plt.show()

# sns.barplot(x="pclass",y="survived",data=titanic,palette='rocket')
# plt.show()

# sns.barplot(x="pclass",y="survived",data=titanic,palette='vlag')
# plt.show() 

# # Instead of Palette and hue attributes you can directly use color attribute

# sns.barplot(x="pclass",y="survived",data=titanic,color='purple')
# plt.show() 

# SeaBorn Scatter plot  - It is used to understand relationship between two numerical entities

# sns.scatterplot(x="sepal_length",y="petal_length",data=iris)
# plt.show()

# #Species column will map color
# sns.scatterplot(x="sepal_length",y="petal_length",data=iris,hue="species",style="species",palette="rocket")
# plt.show()

# # Distribution Plot/SeaBorn Histogram
# sns.distplot(diamonds['price'],color='purple')  
# plt.show()
#  # When hist=False we only get frequency curve 
# sns.distplot(diamonds['price'],hist=False,color='purple')
# plt.show()
# # When only we want histogram then kde=false 
# sns.distplot(diamonds['price'],color='purple',kde=False) # To just get the 10 bins you can write bins=10
# plt.show()

# # If we want to map it vertically 
# sns.distplot(diamonds['price'],color='purple',kde=False,vertical=True)
# plt.show()


# # SeaBorn Jointplot
# sns.jointplot(x='sepal_length',y='petal_length',data=iris,color='indigo',kind='reg')  # we get histogram on the back and scatterplot at the forward side
# plt.show()

# SeaBorn Box plot
sns.boxplot(x="size",y="tip",data=tips,color='crimson',linewidth=2)
plt.show()

sns.boxplot(x='size',y='tip',data=tips,palette="deep",linewidth=2)
plt.show()

# palette names - vlag,rocket,Blues_d,deep,Set1,pastel,muted,bright,light,dark,colorblind
order = tips.groupby("day")["total_bill"].median().sort_values().index
sns.boxplot(x="day",y="total_bill",data=tips,order=order,hue="size",linewidth=2)
plt.show()
