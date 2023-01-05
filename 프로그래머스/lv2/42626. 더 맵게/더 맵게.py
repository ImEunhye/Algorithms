import heapq

def solution(scoville, K):
    answer = 0
    
    heap = []
    for sco in scoville:
        heapq.heappush(heap, sco)

    while 1:
        if len(heap) < 2 : break
        first = heapq.heappop(heap)
        
        if first >= K : #만족
            break
        
        second = heapq.heappop(heap)
        new = first + second * 2
        
        heapq.heappush(heap, new)
        answer += 1
        
    
    if (min(heap)<= K): answer = -1
        
    return answer