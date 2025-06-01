import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
random.seed = 42
import warnings
warnings.filterwarnings("ignore")

# Synthetically create a sample with random and independent observations

# Let us use a sample of synthetic data (from some disb) 
# we generated so that we know the population medain to compare against
# Let sample from Beta disb with alpha = 2,beta=2 which has a population median of 0.5
# Refer: https://en.wikipedia.org/wiki/Beta_distribution Median ~ (alpha-1/3)/(alpha+beta-2/3) if alpaha, beta >1
n=100;
S = np.random.beta(2,2,n) # data can have any distribution.

#Q. Given S, how to estimate the popualtion median?

# function to generate a bootstrap(sampling with repalcement) sample of size n given a sample S. Each sample 
def bootstrapSample(S, m):

  n = S.size; # size of S
  indx = np.random.randint(n, size=m) # generates random integer indices from discrete unif random disb
  r = S[indx]
  return r


m = 50; # size of each bootstap sample
k = 1000; # number of botostrap samples

medians = np.zeros(k)

for i in range(k):
  medians[i] = np.median(bootstrapSample(S, m))

print(medians.size)

# Now estimate median
print(np.mean(medians))

print(np.median(medians))

sns.set()
ax = sns.distplot(medians)
plt.show()


# 95% C.I on the medain estimate with n=100, m=50, k=1000

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.percentile.html
lb_M = np.percentile(medians,2.5)
ub_M = np.percentile(medians,97.5)
mid_M = np.percentile(medians,50)

print(lb_M, mid_M, ub_M)





# same experiment as above with same S, n=100, m=100, k=1000
n=100
m=100 # size of each bootstap sample
k=1000  # number of botostrap samples

medians = np.zeros(k)

for i in range(k):
  medians[i] = np.median(bootstrapSample(S, m))

print(medians.size)

lb_M = np.percentile(medians,2.5)
ub_M = np.percentile(medians,97.5)
mid_M = np.percentile(medians,50)

print(lb_M, mid_M, ub_M)


# same experiment as above with same S, n=100, m=200, k=1000
n=100
m=200 # size of each bootstap sample
k=1000  # number of botostrap samples

medians = np.zeros(k)

for i in range(k):
  medians[i] = np.median(bootstrapSample(S, m))

print(medians.size)

lb_M = np.percentile(medians,2.5)
ub_M = np.percentile(medians,97.5)
mid_M = np.percentile(medians,50)

print(lb_M, mid_M, ub_M)