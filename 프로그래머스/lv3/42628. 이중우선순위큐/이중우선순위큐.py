import heapq

def solution(operations):
    heap = []
    
    for operation in operations:
        op1, op2 = operation.split()
        if op1 == 'I':
            heapq.heappush(heap, int(op2))
            print(heap)
        elif (op1 == 'D') and (len(heap)>0):
            if op2 == '-1':
                heapq.heappop(heap)
            else:
                max_ = max(heap)
                heap.remove(max_)
        
    if len(heap)<1: return [0,0]
    
    return [max(heap), min(heap)]
 