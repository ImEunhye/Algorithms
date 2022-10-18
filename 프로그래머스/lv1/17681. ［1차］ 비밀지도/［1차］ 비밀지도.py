def solution(n, arr1, arr2):
    answer = []
    
    for num1,num2 in zip(arr1,arr2):
        bin1 = list(bin(num1))[2:]#이진법으로 변환 후 리스트로 저장
        bin2 = list(bin(num2))[2:]
        
        if len(bin1)<n:#자릿수를 맞춤
            for i in range(n-len(bin1)):
                bin1.insert(i,'0')
        if len(bin2)<n:
            for i in range(n-len(bin2)):
                bin2.insert(i,'0')
        
        str1 =''
        for b1, b2 in zip(bin1,bin2):
            if b1 == '1' or b2 == '1':
                str1 += '#'
            else: 
                str1 += ' '
        answer.append(str1)
        
#     for i in range(len(arr1)):
#         bin_1 = bin(arr1[i]).split('b')[1]
#         bin_2 = bin(arr2[i]).split('b')[1]
#         if len(bin_1) < n : bin_1 = '0'*(n-len(bin_1)) + bin_1
#         if len(bin_2) < n : bin_2 = '0'*(n-len(bin_2)) + bin_2
#         arr1[i] = bin_1
#         arr2[i] = bin_2
    
#     for i in range(len(arr1)):
#         ans = ''
#         for j in range(n):
#             if (arr1[i][j] == '1' or arr2[i][j] == '1') : char_ = '#'
#             else: char_ = ' '
#             ans += char_
#         answer.append(ans)           
        
    return answer