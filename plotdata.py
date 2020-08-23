import numpy as np


# define empty list
data = []

# open file and read the content in a list
with open('result_50.txt', 'r') as f:
    filecontents = f.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        val = line[:-1]

        # add item to the list
        data.append(int(val))


# print(data)

# print(type(data[1]))

# x = np.random.randint(low=0, high=100, size=100)
x = np.array(data)
# print(x)
# print(type(x))

# Compute frequency and bins
frequency, bins = np.histogram(x, bins=20, range=[0, 150])

# Pretty Print
for b, f in zip(bins[1:], frequency):
    print(round(b, 1), ' '.join(np.repeat('*', f)))

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

# Plot Histogram on x
x = np.random.normal(size = 1000)
plt.hist(x, bins=50)
plt.gca().set(title='Frequency Histogram', ylabel='Frequency');



#  import numpy as np
# from matplotlib import pyplot as plt

# def my_dist(x):
#     return np.exp(x)

# print(my_dist)

# x = np.arange(1, 200)
# p = my_dist(x)
# plt.plot(x, p)
# plt.show()




# import numpy as np
# from matplotlib import pyplot as plt

# def my_dist(x):
#     return np.exp(-x ** 2)

# x = np.arange(-100, 100)
# p = my_dist(x)
# plt.plot(x, p)
# plt.show()



# import numpy as np
# from scipy.interpolate import UnivariateSpline
# from matplotlib import pyplot as plt

# N = 1000
# n = N//10
# s = np.random.normal(size=N)   # generate your data sample with N elements
# p, x = np.histogram(s, bins=n) # bin it into n = N//10 bins
# x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
# f = UnivariateSpline(x, p, s=n)
# plt.plot(x, f(x))
# plt.show()

# from matplotlib import pyplot as plt

# from scipy.stats.kde import gaussian_kde
# from scipy.stats.kde import kde 
# from numpy import linspace
# # create fake data
# data = randn(1000)
# # this create the kernel, given an array it will estimate the probability over that values
# kde = gaussian_kde( data )
# # these are the values over wich your kernel will be evaluated
# dist_space = linspace( min(data), max(data), 100 )
# # plot the results
# plt.plot( dist_space, kde(dist_space) )