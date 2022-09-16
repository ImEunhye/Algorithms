def solution(x):
    return not(x % sum(list(map(int,[i for i in str(x)]))))
    