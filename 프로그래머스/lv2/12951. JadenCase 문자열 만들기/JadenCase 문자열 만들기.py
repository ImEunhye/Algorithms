def solution(s):
    s_arr = list(s)
    if s_arr[0].isalpha : s_arr[0] = s_arr[0].upper()
    for i in range(1,len(s_arr)):
        if s_arr[i-1] == ' ' and s_arr[i] != ' ':
            s_arr[i] = s_arr[i].upper()
        elif (s_arr[i] != ' '):
            s_arr[i] = s_arr[i].lower()

    return ''.join(s_arr)

        