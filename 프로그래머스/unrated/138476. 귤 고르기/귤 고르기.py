from collections import Counter

def solution(k, tangerine):
    answer = 0

    counter = Counter(tangerine)
    sort_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    
    for counter in sort_counter :
        k -= counter[1]
        answer += 1
        if k <= 0:
            break
        
    return answer