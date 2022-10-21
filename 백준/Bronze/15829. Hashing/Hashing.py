n = int(input())
str_list = list(input())
sum = 0

for i in range(n):
    sum += (ord(str_list[i])-96) * (31**i)

print(sum%1234567891)
