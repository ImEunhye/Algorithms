n = int(input())
humans = []
answer = [1]* n
for i in range(n):
    humans.append(list(map(int,input().split())))

for human in humans:
    for i in range(len(humans)):
        if (human[0]>humans[i][0]) and (human[1]>humans[i][1]):
            answer[i]+= 1

print(*answer)