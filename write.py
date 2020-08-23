nums = [1,2,3,4]

# f = open("demofile2.txt", "a")

# for item in nums:
#     f.writelines(str(item))


f=open('log.txt','a')
my_list=map(lambda x:x+'\n', str(nums))
f.writelines(my_list)
f.close()

# with open('result_1.txt', 'w') as filehandle:
#     filehandle.write(val for val in nums)