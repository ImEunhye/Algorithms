from collections import deque

n = int(input())
card_list = deque(range(1,n+1))
while len(card_list)>1:
    card_list.popleft()
    card_list.append(card_list.popleft())
print(card_list[0])