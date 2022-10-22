def solution(price, money, count):
    sum_ = 0
    for i in range(count):
        sum_ += price * (i+1)
    if sum_ < money:
        return 0
    return sum_-money