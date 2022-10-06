def solution(n, m):
    if n > m: n,m = m,n
    for i in range(1,n+1):
        if n%i ==0 and m%i==0:
            max = i
    for i in range(n,n*m+1,n):
        if i%m == 0:
            min = i 
            break
    answer = [max,min]
    return answer