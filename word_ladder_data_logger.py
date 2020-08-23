
import subprocess
import sys


result_list = []
cleaned_list = []

for i in range(5000):
    result_list.append(subprocess.run([sys.executable, "word_ladder_a.py"], capture_output=True, text=True ))
    # result = (subprocess.run([sys.executable, "word_ladder_a.py"], capture_output=True, text=True ))
    # result = subprocess.run([sys.executable, "word_ladder_a.py"])
    # result_list.append(subprocess.run([sys.executable, "word_ladder_a.py"]))   NO


# print("stdout:", result.stdout)    
print(f' result_list  {result_list}')

for item in result_list:
    # print(f' \t item {item.stdout}  {type(item.stdout)} ')
    # cleaned_list.append( int(item.stdout.split(",")[-1][:-2].strip())  )
    cleaned_list.append( item.stdout.split(",")[-1][:-2].strip() )

# str = "(['bit', 'kit', 'kip'], 102)"
# print(str.split(",")[-1][:-1])

#  print(f' cleaned_list {cleaned_list}')

max = max(cleaned_list)
min = min(cleaned_list)
print(f' max {max}  min {min}')


with open('result_1.txt', 'w') as f:
    for item in cleaned_list:
        # f.write('%s\n' % item)
        f.write(f'{item}\n')






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
