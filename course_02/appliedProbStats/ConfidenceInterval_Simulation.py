import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random

# Set seed correctly
random.seed(42)

import warnings
warnings.filterwarnings("ignore")

import plotly.offline as offline
import plotly.graph_objs as go
offline.init_notebook_mode()

from mpl_toolkits.mplot3d import Axes3D
from prettytable import PrettyTable
import scipy.stats as st

# z-scores
print("zScore for 0.1 probability to right is", st.norm.ppf(1 - 0.10))
print("zScore for 0.25 probability to left is", st.norm.ppf(0.25))

# Load dataset
df = pd.read_csv('train.csv')
print(df)

# Filter male data
data_male = np.array(df[df['Gender'] == 'M']['Purchase'].values)
samples = random.sample(range(0, data_male.shape[0]), 50)
print("The mean of money spent by sample set of 50 persons:", data_male[samples].mean())
print("Given that we have population standard deviation: 5051")
print("From CLT we can say that the std of sampling distribution of the sample mean is σ/√n:", 5051 / 10)

# Full population data
data = np.array(df['Purchase'].values)
print("Number of samples in our data:", data.shape[0])
sns.histplot(data, kde=True, color='g')

# Calculate population mean and std
population_mean = np.round(data.mean(), 3)
population_std = np.round(data.std(), 3)

# Sampling function
def get_means_of_n_samples_with_m_size(data, n, m):
    sample_mean_m_samples_n_ele = []
    for i in range(n):
        samples = random.sample(range(0, data.shape[0]), m)
        sample_mean_m_samples_n_ele.append(data[samples].mean())
    return sample_mean_m_samples_n_ele

sample_means = dict()
sample_means['100samples_50ele'] = get_means_of_n_samples_with_m_size(data,100, 50)
sample_means['1000samples_50ele'] = get_means_of_n_samples_with_m_size(data,1000, 50)

sample_means['100samples_100ele'] = get_means_of_n_samples_with_m_size(data,100, 100)
sample_means['1000samples_100ele'] = get_means_of_n_samples_with_m_size(data,1000, 100)

sample_means['100samples_1000ele'] = get_means_of_n_samples_with_m_size(data,100, 1000)
sample_means['1000samples_1000ele'] = get_means_of_n_samples_with_m_size(data,1000, 1000)

# Colors and subplot positions
colrs = ['r', 'g', 'b', 'y', 'c', 'm']
plt_grid = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]

fig, axs = plt.subplots(3, 2, figsize=(15, 10))


def plt_confidence_interval(data, sample_mean, population_std, i, j, color):
    sns.distplot(data, color=color, ax=axs[i, j])
    axs[i, j].axvline(data.mean(), linestyle="-", color='k', label="p_mean")
    axs[i, j].axvline(sample_mean, linestyle="--", color='m', label="s_mean")
    axs[i, j].axvline(sample_mean+2*(population_std/np.sqrt(100)), linestyle=":", color='g', label="s_mean+2*SE")
    axs[i, j].axvline(sample_mean-2*(population_std/np.sqrt(100)), linestyle=":", color='g', label="s_mean-2*SE")
    axs[i, j].legend()

fig, axs = plt.subplots(3, 2,  figsize=(15, 10))
for i in range(6):
    sample = data_male[random.sample(range(0, data_male.shape[0]), 100)]
    plt_confidence_interval(data_male, np.array(sample).mean(), population_std, plt_grid[i][0],plt_grid[i][1],colrs[i])
plt.show()