
def solution(s):
    answer = True
    a,b = 0,0
    if s[0] == ')' : return False
    for ss in s :
        if ss == '(' : a += 1
        else: b += 1
        if b>a : return False
    if a != b : return False
    return answer