import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    que = deque()
    cnt = 0
    
    for p,s in zip(progresses,speeds):
        days = math.ceil((100-p)/s)
        que.append(days)
    
    while len(que)>0:
        now = que.popleft()
        for s in que:
            if now >= s:
                cnt += 1
            else:
                break
                
        if cnt == 0 :
            answer.append(1)
        else:
            answer.append(cnt+1)
            for _ in range(cnt):
                que.popleft()
            cnt = 0
            

    return answer