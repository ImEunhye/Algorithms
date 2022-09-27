def solution(n):
    answer = 1
    for i in range(1,int(n/2)+1):
        for j in range(i+1,int(n/2)+2):
            sum_ = sum(list(range(i,j+1)))
            if sum_ == n: 
                answer+= 1 
            if sum_ > n : break
    return answer