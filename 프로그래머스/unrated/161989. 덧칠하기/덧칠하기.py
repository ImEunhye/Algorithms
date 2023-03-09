def solution(n, m, section):
    answer = 0
    while len(section):
        num = section.pop()
        while len(section):
            if num-m < section[-1]:
                section.pop()
            else: 
                break
        answer += 1        
    
    return answer