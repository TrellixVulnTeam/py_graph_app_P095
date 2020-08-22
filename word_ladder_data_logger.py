
import subprocess
import sys

result_list = []
cleaned_list = []

for i in range(500):
    result_list.append(subprocess.run([sys.executable, "word_ladder_a.py"], capture_output=True, text=True ))
    # result = (subprocess.run([sys.executable, "word_ladder_a.py"], capture_output=True, text=True ))
    # result = subprocess.run([sys.executable, "word_ladder_a.py"])
    # result_list.append(subprocess.run([sys.executable, "word_ladder_a.py"]))   NO


# print("stdout:", result.stdout)    
print(f' result_list  {result_list}')

for item in result_list:
    print(f' \t item {item.stdout}  {type(item.stdout)} ')
    # cleaned = item.stdout.split(",")[-1][:-1]
    # cleaned_list.append(cleaned)
    cleaned_list.append( int(item.stdout.split(",")[-1][:-2].strip())  )

# str = "(['bit', 'kit', 'kip'], 102)"
# print(str.split(",")[-1][:-1])

print(f' cleaned_list {cleaned_list}')

