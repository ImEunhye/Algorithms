
def solution(p):
    if p == '' :
        return p
    
    answer = ''
    u1,u2 = 0,0
    v1,v2 = 0,0
    
    for i in range(len(p)):
        if p[i] == '(':
            u1 += 1
        else :
            u2 += 1
        if u1 == u2:
            u = p[:i+1]
            v = p[i+1:]
            break
    
    if u[0] == "(": #올바른 괄호 문자열일때
        return u + solution(v)
    else: # 아닐 때
        new_u = ""
        for i in u[1:-1]:
            if i == "(":
                new_u += ")"
            else:
                new_u += "("
                
        return "(" + solution(v)+ ")" + new_u
        