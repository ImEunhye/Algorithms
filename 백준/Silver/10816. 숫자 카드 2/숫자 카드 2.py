n = int(input())
cards = sorted(list(map(int,input().split())))
m = int(input())
check = list(map(int,input().split()))

def b_search(cards,num, left, right):
    while left<=right :
        mid = (left+right)//2
        if cards[mid]>num:
            right = mid-1
            return b_search(cards,num,left,right)
        elif cards[mid]<num:
            left = mid+1
            return b_search(cards,num,left,right)
        elif cards[mid] == num:
            return count.get(num)
    return 0
    
count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for i in range(m):
    print(b_search(cards,check[i],0,n-1),end = ' ')
