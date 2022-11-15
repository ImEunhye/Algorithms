def solution(numbers):
    nums = list(range(0,10))

    return sum([x for x in nums if x not in numbers])