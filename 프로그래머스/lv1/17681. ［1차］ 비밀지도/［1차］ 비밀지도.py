def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        bin_1 = bin(arr1[i]).split('b')[1]
        bin_2 = bin(arr2[i]).split('b')[1]
        if len(bin_1) < n : bin_1 = '0'*(n-len(bin_1)) + bin_1
        if len(bin_2) < n : bin_2 = '0'*(n-len(bin_2)) + bin_2
        arr1[i] = bin_1
        arr2[i] = bin_2
    
    for i in range(len(arr1)):
        ans = ''
        for j in range(n):
            if (arr1[i][j] == '1' or arr2[i][j] == '1') : char_ = '#'
            else: char_ = ' '
            ans += char_
        answer.append(ans)           
        
    return answer