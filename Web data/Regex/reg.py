#read the file and count no. of digits

import re

file = open('regex_sum_33840.txt')

lines = file.readlines()

totalSum = 0
for line in lines:
    line = line.rstrip()
    nums = re.findall('([0-9]+)', line)
    if len(nums) > 0:
        nums = map(int, nums)
        localSum = sum(nums)
        totalSum += localSum

print (totalSum)