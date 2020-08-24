import numpy as np
from scipy.interpolate import UnivariateSpline
from matplotlib import pyplot as plt

# generate data samples
# data = scipy.stats.expon.rvs(loc=0, scale=1, size=1000, random_state=123)



# define empty list
data_list = []

# open file and read the content in a list
with open('result_5000.txt', 'r') as f:
    filecontents = f.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        val = line[:-1]

        # add item to the list
        # data.append(int(val))
        data_list.append(float(val))



data = np.array(data_list)


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