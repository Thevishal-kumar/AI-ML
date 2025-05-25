import matplotlib.pyplot as plt
import numpy as np
# plt.plot([2,4, 6, 4])
# plt.ylabel("Numbers")
# plt.xlabel('Indices')
# plt.title('MyPlot')
# plt.grid() 
# plt.show()


# t = np.arange(0., 5., 0.2) 

# #blue dashes, red squares and green triangles
# plt.plot(t, t**2, 'b--', label='^2')#   'rs',   'g^')
# plt.plot(t,t**2.2, 'rs', label='^2.2')
# plt.plot(t, t**2.5, 'g^', label='^2.5')
# plt.grid()
# # plt.legend() # add legend based on line labels
# plt.show()

# x1 = [1, 2, 3, 4]
# y1 = [1, 4, 9, 16]
# x2 = [1, 2, 3, 4]
# y2 = [2, 4, 6, 8]
# lines = plt.plot(x1, y1, x2, y2)

# # use keyword args
# plt.setp(lines[0], color='r', linewidth=2.0)

# # or MATLAB style string value pairs
# plt.setp(lines[1], 'color', 'g', 'linewidth', 2.0)

# plt.grid()
# plt.show()  


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
# The subplot() command specifies numrows, numcols, 
# fignum where fignum ranges from 1 to numrows*numcols.
plt.subplot(211)
plt.grid()
plt.plot(t1, f(t1), 'b-')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()
