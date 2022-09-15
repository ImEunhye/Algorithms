def solution(n):
    str1 = ''
    li1 = sorted(str(n))[::-1]
    for c in li1:
        str1 += c
    return int(str1)

    