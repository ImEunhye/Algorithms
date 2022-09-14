def solution(s, n):
    answer = ''
    d = int(n / 26)
    n = n % 26
    
    for char in s:
        if char != ' ':
            if chr(ord(char)+n).isalpha():
                if (65<=ord(char)<=90) and (97<=ord(char)+n<=122):
                    char = chr(ord(char)+n-26*(d+1))
                else: 
                    char = chr(ord(char)+n)
            elif not(chr(ord(char)+n).isalpha()):
                char = chr(ord(char)+n-26*(d+1))
        answer += char
    print(answer)
    return answer
    