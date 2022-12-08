def solution(s):
    answer = '';
    numbers = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i:i+3] in numbers:
                answer += numbers[s[i:i+3]]
            elif s[i:i+4] in numbers:
                answer += numbers[s[i:i+4]]
            elif s[i:i+5] in numbers:
                answer += numbers[s[i:i+5]]
        else:
            answer += s[i]
            
    return int(answer)