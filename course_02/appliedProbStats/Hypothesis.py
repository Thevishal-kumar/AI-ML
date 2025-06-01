# 📦 Import Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import warnings
from prettytable import PrettyTable
from IPython.display import HTML, display
import plotly.offline as offline
import plotly.graph_objs as go
from mpl_toolkits.mplot3d import Axes3D

# ⚙️ Setup
random.seed(42)
warnings.filterwarnings("ignore")
offline.init_notebook_mode()

# 📥 Load Dataset
df = pd.read_csv('train.csv')
print("Number of data points in our population:", df.shape)
print("% of missing values in 'Purchase':", df['Purchase'].isnull().sum() * 100 / len(df))
df.head(2)

# 📊 Initial Population Stats
data = np.array(df['Purchase'].values)
print("Number of samples in our data:", data.shape[0])
sns.distplot(data, color='g')

# Population Mean & Std
population_mean = np.round(data.mean(), 3)
population_std = np.round(data.std(), 3)

# 📉 Plot CDF with Threshold
def plt_cdfplot_withthreshold(j, c, difference, threshold, sample):
    sns.kdeplot(difference, cumulative=True, color=c, ax=axs[j])
    axs[j].axvline(threshold, linestyle="--", color='r', label=int(threshold))
    axs[j].set_title("CDF of differences for " + str(sample) + " samples")
    axs[j].legend()
    axs[j].grid()

# 📈 Compare Sample Means
def diff_in_samples(dist1, dist2, gender1, gender2):
    print(f"The average spendings {len(dist1)} {gender1} =", dist1.mean())
    print(f"The average spendings {len(dist2)} {gender2} =", dist2.mean())
    diff_in_mean = dist1.mean() - dist2.mean()
    print(f"The difference between mean of {gender1} and {gender2} =", diff_in_mean)
    return diff_in_mean

# 🧪 Hypothesis Testing Function
def calculate_p_value(sample1, sample2, diff, alpha):
    difference = []
    total_sample = np.concatenate((sample1, sample2))
    
    for _ in range(1000):
        samples = random.sample(range(0, len(total_sample)), 100)
        set1 = total_sample[samples[:50]].mean()
        set2 = total_sample[samples[50:]].mean()
        difference.append(set1 - set2)
    
    difference.sort()
    count = sum(((i > diff) and (i > 0)) for i in difference)
    pValue = count / len(difference)
    
    print("Percentage of values greater than the difference", diff, "=", pValue * 100, "%")
    print("The p-value =", pValue, "| Significance level α =", alpha)
    
    if pValue > alpha:
        print("🔸 We fail to reject the null hypothesis.")
    else:
        print("✅ We reject the null hypothesis.")
    
    print('_' * 50)
    return difference

# 🔍 Hypothesis Testing for Male vs Female Purchases
data_female = np.array(df[df['Gender'] == 'F']['Purchase'].values)
data_male = np.array(df[df['Gender'] == 'M']['Purchase'].values)
sample_sizes = [100, 500, 1000]
alpha = 0.15

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
colrs = ['r', 'g', 'b']

for j, i in enumerate(sample_sizes):
    print(f"\n--- For Sample Size: {4*i} ---")
    
    female_sample = data_female[random.sample(range(0, data_female.shape[0]), i)]
    male_sample = data_male[random.sample(range(0, data_male.shape[0]), i)]
    
    diff_in_mean = diff_in_samples(male_sample, female_sample, "male", "female")
    differences = calculate_p_value(male_sample, female_sample, diff_in_mean, alpha)
    
    plt_cdfplot_withthreshold(j, colrs[j], differences, threshold=diff_in_mean, sample=i)
