import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

# define empty list
data = []

# open file and read the content in a list
with open('result_100.txt', 'r') as f:
    filecontents = f.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        val = line[:-1]

        # add item to the list
        # data.append(int(val))
        data.append(float(val))







hist, bins = np.histogram(data, bins=10, normed=True)
data = (data[1:] + data[:-1] - data[0]) / 2
plt.plot(data, hist)


# import scipy.stats.kde
# import numpy as np
# import pandas as pd


# # define empty list
# data = []

# # open file and read the content in a list
# with open('result_100.txt', 'r') as f:
#     filecontents = f.readlines()

#     for line in filecontents:
#         # remove linebreak which is the last character of the string
#         val = line[:-1]

#         # add item to the list
#         # data.append(int(val))
#         data.append(float(val))



# s = pd.Series([1, 2, 2.5, 3, 3.5, 4, 5])

# ax = s.plot.kde()
# ax.plot()



# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))

# ts = ts.cumsum()

# ts.plot()