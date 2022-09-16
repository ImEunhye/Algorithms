def solution(array, commands):
    answer = []
    for com in commands:
        li1  = array[com[0]-1:com[1]]
        answer.append(sorted(li1)[com[2]-1])
    return answer
