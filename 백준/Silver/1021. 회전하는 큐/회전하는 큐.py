n,m = map(int, input().split())
nums = list(map(int, input().split()))
circular_q = list(range(1,n+1))
front = 0
cnt = 0

for num in nums:
    index = circular_q.index(num)
    cnt += min(abs(index-front),abs(front+(len(circular_q)-index)),abs(index+(len(circular_q)-front)))
    front = (index)%len(circular_q)
    circular_q.remove(num)
print(cnt)