def solution(priorities, location):
    answer = 0
    while 1 :
        if priorities[0] == max(priorities):
            answer += 1
            priorities.pop(0)
            location -= 1
            

        if location == -1 : 
            break
            
        if priorities[0] < max(priorities):
            num = priorities.pop(0)
            priorities.append(num)
            if location == 0 : location = len(priorities)-1
            else : location -=1
    return answer
