def recursive_func(sign, cnt, sum_, numbers, sum_list):
    if cnt == len(numbers):
        return
    
    if sign == '+':
        sum_ += numbers[cnt]
    elif sign == '-': 
        sum_ -= numbers[cnt]
    
    cnt += 1
    
    recursive_func('+', cnt, sum_, numbers, sum_list)
    recursive_func('-', cnt, sum_, numbers, sum_list)
    
    if cnt == len(numbers):
        sum_list.append(sum_)


def solution(numbers, target):
    answer = 0
    cnt = 0
    sum_ = 0
    sum_list = []

    recursive_func('+', cnt, sum_, numbers, sum_list)
    recursive_func('-', cnt, sum_, numbers, sum_list)


    for sum_ in sum_list:
        if sum_ == target:
            answer += 1
            
    return answer

