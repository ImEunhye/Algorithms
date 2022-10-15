import math

nums = []
num = input()
while num != '0':
    nums.append(num)
    num = input()


def factorial(num):
    fac_num = 0
    for i in range(len(num)):
        fac_num += int(num[i]) * math.factorial(len(num)-i)

    return fac_num


for num in nums:
    num = list(num)
    print(factorial(num))

