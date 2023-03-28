from collections import deque
def solution(people, limit):
    if sum(people)<=limit: return 1

    answer = 0
    q = deque(sorted(people))

    while len(q)>1:
        if q[0]+q[-1]<= limit:
            q.popleft()
            q.pop()
        else:
            q.pop()
        
        answer += 1
    if len(q)== 1:
        answer += 1
    
    return answer