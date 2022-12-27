seconds = int(input())
button_list = [300,60,10]
cnt_list = [0,0,0]

for i in range(len(button_list)):
    cnt_list[i] = seconds//button_list[i]
    seconds -= button_list[i]*(seconds//button_list[i])

if seconds != 0:
    print(-1)
else:
    print(*cnt_list)