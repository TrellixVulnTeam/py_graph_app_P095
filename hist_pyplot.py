import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import statistics





# define empty list
data = []

# open file and read the content in a list
with open('result_50.txt', 'r') as f:
    filecontents = f.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        val = line[:-1]

        # add item to the list
        # data.append(int(val))
        data.append(float(val))

d_mean = statistics.mean(data)
d_max = max(data)
d_min = min(data)
d_mode = statistics.mode(data)
d_stdev = statistics.stdev(data)

# example data
mu = str(d_mean) # mean of distribution
sigma = str(d_stdev) # standard deviation of distribution
# x = mu + sigma * np.random.randn(10000)

print(f' mu {mu} sigma {sigma} mode {str(d_mode)}')
print(f' min {str(d_min)} max {str(d_max)} ')


# 500
# mu 81.926 sigma 35.2815830740121 
# mu 83.5358 sigma 36.0183756301781
# 5000
# mu 83.5358 sigma 36.0183756301781 mode 134.0

x = np.array(data)

# mu = statistics.mean(data)
# sigma = statistics.stdev(data)

# x = np.array(data)

n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('# sets to find solution\n min 19 max 134 ')
plt.ylabel('Probability')
plt.title("50 loops of find_word_path('bit', 'kip')")
plt.text(60, .025, r'$\mu=88.4,\ \sigma=38.5  \ mode = 107 $ ')
plt.xlim(10, 160)
plt.ylim(0, 0.05)
plt.grid(True)
plt.show()