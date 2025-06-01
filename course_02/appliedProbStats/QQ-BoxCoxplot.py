import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# x = np.random.normal(loc = 20, scale = 5, size=100)
# stats.probplot(x, dist="norm", plot=plt)
# plt.grid()
# plt.show()

import seaborn as sns
# x = np.random.exponential(scale=1.0, size=1000)

# # plot PDF(X)

# sns.set()
# ax = sns.distplot(x)
# plt.show()

# plot CDF(X)
# kwargs = {'cumulative': True}
# sns.distplot(x, hist_kws=kwargs, kde_kws=kwargs)
# plt.grid()
# plt.show()


# QQ-Plot

# stats.probplot(x, dist="norm", plot=plt)
# plt.grid()
# plt.show()





#Box-cox
# x_t, l = stats.boxcox(x) # l=lambda, x_t =x tranformed by box-cox
# print(l)

#QQ-Plot
# stats.probplot(x_t, dist="norm", plot=plt)
# plt.grid()
# plt.show()


# PDF of x_t
# sns.histplot(x_t, kde=True)
# plt.grid()
# plt.show()

#CDF of x_t
# kwargs = {'cumulative': True}
# sns.histplot(x_t, kde=True, cumulative=True)
# plt.grid()
# plt.show()



# PARETO DISTRIBUTION
x = np.random.pareto(a=3.0, size=1000) * 1.0  # 'a' is shape, multiply for scale

# Plot PDF
# sns.set()
# sns.histplot(x, kde=True, stat="density", bins=50)
# plt.title("PDF of Pareto-Distributed Data")
# plt.xlabel("x")
# plt.ylabel("Density")
# plt.show()

# CDF
kwargs = {'cumulative': True}
sns.distplot(x, hist_kws=kwargs, kde_kws=kwargs)
plt.grid()
plt.show()