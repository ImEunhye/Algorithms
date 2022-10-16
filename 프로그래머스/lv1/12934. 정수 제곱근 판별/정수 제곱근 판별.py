def solution(n):
    if n == 1 : return 4
    for i in range(1,n):
        if n /i == i and n %i == 0:
            answer = i
            return (answer+1)**2
    return -1