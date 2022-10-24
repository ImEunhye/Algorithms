def solution(phone_book):
    answer = True
    phone_book.sort()
   
    for i in range(len(phone_book)-1):
        length = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:length]:
            answer = False
            break
    return answer