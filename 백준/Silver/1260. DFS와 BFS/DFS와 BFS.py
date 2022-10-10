from collections import deque

n,m,v= map(int,input().split())
lines = []
for _ in range(m):
    lines.append(input())

line_dict = {} # 이어진 점들을 딕셔너리로 저장
for i in range(1,n+1):
    line_dict[i] = []

for i in range(1,n+1):
    for j in lines:
        a,b = map(int,j.split())
        if a == i :
            line_dict[i].append(b)
        if b == i :
            line_dict[i].append(a)

def dfs(v, line_dict):
    dfs_ans = []
    note = v
    stack = []
    tmp =line_dict[v].copy()
 
    tmp.sort(reverse = True)
    stack = tmp
    dfs_ans.append(note)
    
    while len(stack)>0:
        now = stack.pop()
      
        if now not in dfs_ans:
            note = now
            dfs_ans.append(now)
            
        else: continue

        if now in list(line_dict.keys()):
            line_dict[now].sort(reverse=True)
            stack.extend(line_dict[now])

    return dfs_ans


def bfs(v,line_dict):
    bfs_ans = []
    note = v
    tmp =line_dict[v].copy()
 
    tmp.sort()
    queue = deque(tmp)
    bfs_ans.append(note)
   
    while len(queue)>0:
        now = queue.popleft()
        if now not in bfs_ans:
            note = now
            bfs_ans.append(now)
        else: continue

        if now in list(line_dict.keys()):
            line_dict[now].sort()
            queue.extend(line_dict[now])
            
    return bfs_ans

print(*dfs(v,line_dict))
print(*bfs(v,line_dict))
