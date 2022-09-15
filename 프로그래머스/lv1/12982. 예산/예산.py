def solution(d, budget):
    d = sorted(d)
    sum = 0
    answer = 0
    for num in d:
        sum += num
        answer += 1
        if sum == budget : 
            return answer
        elif sum > budget:
            return answer-1
    return len(d)
