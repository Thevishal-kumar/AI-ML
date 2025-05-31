import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

#generate a gaussian r.v X
x = stats.norm.rvs(size=1000);
sns.set_style('whitegrid')
sns.kdeplot(np.array(x), bw=0.5)
plt.show()
stats.kstest(x, 'norm')





# # Y ~ Continous Uniform Distribution(0,1)
# y = np.random.uniform(0,1,10000);
# sns.kdeplot(np.array(y), bw=0.1)
# plt.show()

# stats.kstest(y, 'norm')