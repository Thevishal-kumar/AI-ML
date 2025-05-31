import random

#load IRIS dataset with 150 points.
from sklearn import datasets
iris = datasets.load_iris()
d = iris.data
d.shape
print(d[0])

# Sample 30 points randomly from the 150 point dataset
n=150
m=30
p = m/n
print(p)
sampled_data =[];

for i in range(0,n):
  a = random.random()
#   print(a)
  if  a <= p:
    sampled_data.append(d[i,:])
    
# print(sampled_data)
print(len(sampled_data))