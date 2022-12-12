from itertools import permutations

def solution(k, dungeons):
    perms = list(permutations(dungeons))
    max_cnt = 0
    for perm in perms:
        cnt = 0
        tired = k
        for i in range(len(perm)):
            if tired >= perm[i][0]:
                tired -= perm[i][1]
                cnt += 1
            else:
                break
        if cnt > max_cnt :
            max_cnt = cnt
    
    return max_cnt