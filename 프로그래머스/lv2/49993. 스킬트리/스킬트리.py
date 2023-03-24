from collections import deque

def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_q = deque(skill)
        flag = True
        
        for s in skill_tree:
            if not s in skill:
                continue
            if skill_q.popleft() != s:
                flag = False
                break
                
        if flag :
            answer += 1
    
    return answer