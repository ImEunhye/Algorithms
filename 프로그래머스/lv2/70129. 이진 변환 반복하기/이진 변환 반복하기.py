def solution(s):
    answer = [0,0]

    while s != '1':
        list_ = list(s)
        count1 = 0
        
        for l in list_:
            if l == '1':
                count1 += 1
                
        answer[0] += 1
        answer[1] += len(s) - count1
        
        s = bin(count1)[2:]
        
    return answer