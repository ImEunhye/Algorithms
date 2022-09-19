def solution(answers):
    answer = []
    answers_len = len(answers)
    arr1 = [1,2,3,4,5]* (int(answers_len/5)) + [1,2,3,4,5][:answers_len%5]
    arr2 = [2,1,2,3,2,4,2,5]* (int(answers_len/8)) + [2,1,2,3,2,4,2,5][:answers_len%8]
    arr3 = [3,3,1,1,2,2,4,4,5,5]* (int(answers_len/10)) + [3,3,1,1,2,2,4,4,5,5][:answers_len%10]
    a = 0
    b = 0
    c = 0
    for i in range(answers_len):
        if answers[i] == arr1[i]: a += 1
        if answers[i] == arr2[i]: b += 1
        if answers[i] == arr3[i]: c += 1

    if max(a,b,c) == a : 
        answer.append(1)
        if a == b: answer.append(2)
        if a == c: answer.append(3)
    elif max(a,b,c) == b: 
        answer.append(2)
        if b == a: answer.append(1)
        if b == c: answer.append(3)
    else: 
        answer.append(3) 
        if c == a: answer.append(1)
        if c == b: answer.append(2)
    
    return sorted(answer)