def solution(s):
    answer = ''
    s_arr = s.split()
    s_arr = list(map(int,s_arr))
    answer += str(min(s_arr)) +' '+ str(max(s_arr))
    return answer