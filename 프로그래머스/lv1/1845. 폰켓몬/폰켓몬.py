from collections import Counter

def solution(nums):
    answer = 0
    num_dict = Counter(nums)
    if len(num_dict.keys()) >= len(nums)/2:
        return len(nums)/2
    else:
        return len(num_dict.keys())
    