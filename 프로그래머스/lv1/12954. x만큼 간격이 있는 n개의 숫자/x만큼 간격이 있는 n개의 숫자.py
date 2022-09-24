def solution(x, n):
    answer = []

    if x > 0:
        answer += range(x,x*n+1,x)
    elif x < 0:
        answer += range(x,x*n-1,x)
    else :
        for i in range(n):
            answer.append(0)
    return answer