#경우의 수 구하는게 잘못됐습니당 간단히 얼굴 3개, 상의 2개, 하의 2개라면. 얼굴 총 4개(안사용포함) * 상의3개(안사용포함) * 하의3개(안사용포함) -1(전부안사용)으로해보셔요
def solution(clothes):
    answer = 1
    clothes_dict = {}
    for clothe, category in clothes:
        if category in clothes_dict.keys(): 
            clothes_dict[category] += 1
        else:
            clothes_dict[category] = 2
            
    if len(clothes_dict.keys()) == 1: return len(clothes)

    for val in clothes_dict.values():
        answer *= val  
        
    return answer-1