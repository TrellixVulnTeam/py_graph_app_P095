import numpy as np
from scipy.interpolate import UnivariateSpline
from matplotlib import pyplot as plt

N = 1000
n = N//10
s = np.random.normal(size=N)   # generate your data sample with N elements
p, x = np.histogram(s, bins=n) # bin it into n = N//10 bins
x = x[:-1] + (x[1] - x[0])/2   # convert bin edges to centers
f = UnivariateSpline(x, p, s=n)
plt.plot(x, f(x))
plt.show()

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