import numpy as np
x = np.random.randint(low=0, high=100, size=100)

# Compute frequency and bins
frequency, bins = np.histogram(x, bins=10, range=[0, 100])

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


# import numpy as np
# from matplotlib import pyplot as plt

# def my_dist(x):
#     return np.exp(-x ** 2)

# x = np.arange(-100, 100)
# p = my_dist(x)
# plt.plot(x, p)
# plt.show()



# import numpy as np
# x = cleaned_list

# # Compute frequency and bins
# frequency, bins = np.histogram(x, bins=10, range=[min, max])

# # Pretty Print
# for b, f in zip(bins[1:], frequency):
#     print(round(b, 1), ' '.join(np.repeat('*', f)))

# import numpy as np
# import matplotlib.pyplot as plt

# plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

# # Plot Histogram on x
# x = np.random.normal(size = 1000)
# plt.hist(x, bins=50)
# plt.gca().set(title='Frequency Histogram', ylabel='Frequency');