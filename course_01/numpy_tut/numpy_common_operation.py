import numpy as np

a  = np.array([1,2,3,4])

# print(a+1)
# print(a**2)

# b = np.ones(4)+1
# print(a-b)
# print(a*b)

# c = np.diag([1,2,3,4])
# print(c*c)

# print(a==b)


# x  = np.array([1,2,3,4])
# print(x.argmax())

# print(np.all([True,False]))

data = np.loadtxt('populations.txt')

# print(data)

# year , hares,lynxes,carrots = data.T
# print(year) 

population = data[:,1:]
# print(population)

# print(np.argmax(population,axis=1))


print(np.median(population,axis=1))