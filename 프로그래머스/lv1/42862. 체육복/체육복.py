def solution(n, lost, reserve):
    lost2 = []
    for lo in lost:
        if lo in reserve: reserve.remove(lo)
        else: lost2.append(lo) 
        
    lost2.sort()
    reserve.sort()
    
    num = 0
    for lo in lost2:
        if (lo-1) in reserve: 
            num += 1 
            reserve.remove(lo-1)
        elif (lo+1) in reserve:
            num += 1
            reserve.remove(lo+1)
            
    return n - len(lost2) + num
    
    