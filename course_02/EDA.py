import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


iris = pd.read_csv("iris.csv")
# print(iris.shape)
# print(iris.columns)
print(iris["species"].value_counts())

# iris.plot(kind='scatter',x='sepal_length',y='sepal_width')
# plt.show()

# sns.set_style("whitegrid")
# sns.FacetGrid(iris, hue="species", height=4) \
#    .map(plt.scatter, "sepal_length", "sepal_width") \
#    .add_legend()
# plt.show()


# PAIR-PLOT 
# plt.close();
# sns.set_style("whitegrid");
# sns.pairplot(iris, hue="species", size=3);
# plt.show()


# # HISTOGRAM - 1D
# iris_setosa = iris.loc[iris["species"] == "setosa"];
# iris_virginica = iris.loc[iris["species"] == "virginica"];
# iris_versicolor = iris.loc[iris["species"] == "versicolor"];
# #print(iris_setosa["petal_length"])
# plt.plot(iris_setosa["petal_length"], np.zeros_like(iris_setosa['petal_length']), 'o')
# plt.plot(iris_versicolor["petal_length"], np.zeros_like(iris_versicolor['petal_length']), 'o')
# plt.plot(iris_virginica["petal_length"], np.zeros_like(iris_virginica['petal_length']), 'o')

# plt.show()

# HISTOGRAM using seaborn -D 
# sns.FacetGrid(iris, hue="species", height=5) \
#    .map(sns.distplot, "petal_length") \
#    .add_legend();
# plt.show();


# CDF 

# iris_setosa = iris.loc[iris["species"] == "setosa"];
# iris_virginica = iris.loc[iris["species"] == "virginica"];
# iris_versicolor = iris.loc[iris["species"] == "versicolor"];
# counts, bin_edges = np.histogram(iris_setosa['petal_length'], bins=10, 
#                                  density = True)
# pdf = counts/(sum(counts))
# print(pdf);
# print(bin_edges);
# cdf = np.cumsum(pdf)
# plt.plot(bin_edges[1:],pdf);
# plt.plot(bin_edges[1:], cdf)


# counts, bin_edges = np.histogram(iris_setosa['petal_length'], bins=20, 
#                                  density = True)
# pdf = counts/(sum(counts))
# plt.plot(bin_edges[1:],pdf);

# plt.show();
# CDF 
# iris_setosa = iris.loc[iris["species"] == "setosa"];
# iris_virginica = iris.loc[iris["species"] == "virginica"];
# iris_versicolor = iris.loc[iris["species"] == "versicolor"];
# counts, bin_edges = np.histogram(iris_setosa['petal_length'], bins=10, 
#                                  density = True)
# pdf = counts/(sum(counts))
# print(pdf);
# print(bin_edges)

# #compute CDF
# cdf = np.cumsum(pdf)
# plt.plot(bin_edges[1:],pdf)
# plt.plot(bin_edges[1:], cdf)
# plt.show();



# # CDF AND PDF OF ALL DIFFERENT COLOR 
# iris_setosa = iris.loc[iris["species"] == "setosa"];
# iris_virginica = iris.loc[iris["species"] == "virginica"];
# iris_versicolor = iris.loc[iris["species"] == "versicolor"];

# counts, bin_edges = np.histogram(iris_setosa['petal_length'], bins=10, 
#                                  density = True)
# pdf = counts/(sum(counts))
# print(pdf);
# print(bin_edges)
# cdf = np.cumsum(pdf)
# plt.plot(bin_edges[1:],pdf)
# plt.plot(bin_edges[1:], cdf)


# # virginica
# counts, bin_edges = np.histogram(iris_virginica['petal_length'], bins=10, 
#                                  density = True)
# pdf = counts/(sum(counts))
# print(pdf);
# print(bin_edges)
# cdf = np.cumsum(pdf)
# plt.plot(bin_edges[1:],pdf)
# plt.plot(bin_edges[1:], cdf)


# #versicolor
# counts, bin_edges = np.histogram(iris_versicolor['petal_length'], bins=10, 
#                                  density = True)
# pdf = counts/(sum(counts))
# print(pdf);
# print(bin_edges)
# cdf = np.cumsum(pdf)
# plt.plot(bin_edges[1:],pdf)
# plt.plot(bin_edges[1:], cdf)
# plt.show();




# MEAN, VARIANCE ,AND STANDARD DEVIATION 
# iris_setosa = iris.loc[iris["species"] == "setosa"]
# iris_virginica = iris.loc[iris["species"] == "virginica"]
# iris_versicolor = iris.loc[iris["species"] == "versicolor"]
# #Mean, Variance, Std-deviation,  
# print("Means:")
# print(np.mean(iris_setosa["petal_length"]))
# #Mean with an outlier.
# print(np.mean(np.append(iris_setosa["petal_length"],50)))
# print(np.mean(iris_virginica["petal_length"]))
# print(np.mean(iris_versicolor["petal_length"]))

# print("\nStd-dev:")
# print(np.std(iris_setosa["petal_length"]))
# print(np.std(iris_virginica["petal_length"]))
# print(np.std(iris_versicolor["petal_length"]))





#Median, Quantiles, Percentiles, IQR.

# iris_setosa = iris.loc[iris["species"] == "setosa"]
# iris_virginica = iris.loc[iris["species"] == "virginica"]
# iris_versicolor = iris.loc[iris["species"] == "versicolor"]
# print("\nMedians:")
# print(np.median(iris_setosa["petal_length"]))
# #Median with an outlier
# print(np.median(np.append(iris_setosa["petal_length"],50)));
# print(np.median(iris_virginica["petal_length"]))
# print(np.median(iris_versicolor["petal_length"]))


# print("\nQuantiles:")
# print(np.percentile(iris_setosa["petal_length"],np.arange(0, 100, 25)))
# print(np.percentile(iris_virginica["petal_length"],np.arange(0, 100, 25)))
# print(np.percentile(iris_versicolor["petal_length"], np.arange(0, 100, 25)))

# print("\n90th Percentiles:")
# print(np.percentile(iris_setosa["petal_length"],90))
# print(np.percentile(iris_virginica["petal_length"],90))
# print(np.percentile(iris_versicolor["petal_length"], 90))

# from statsmodels import robust
# print ("\nMedian Absolute Deviation")
# print(robust.mad(iris_setosa["petal_length"]))
# print(robust.mad(iris_virginica["petal_length"]))
# print(robust.mad(iris_versicolor["petal_length"]))


# BOX-PLOT 
# sns.boxplot(x='species',y='petal_length', data=iris)
# plt.show()


# VIOLIN-PLOT 
# sns.violinplot(x="species", y="petal_length", data=iris, width=0.8)
# plt.show()



#2D Density plot, contors-plot
iris_setosa = iris.loc[iris["species"] == "setosa"]
iris_virginica = iris.loc[iris["species"] == "virginica"]
iris_versicolor = iris.loc[iris["species"] == "versicolor"]
sns.jointplot(x="petal_length", y="petal_width", data=iris_setosa, kind="kde")
