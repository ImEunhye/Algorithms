num = int(input()) # input 받기
input_list  = []
for i in range(num):
    input_list.append(input())


for i in range(num):  
    stop_flag = False
    p_list = list(input_list[i])
    stk = []
  
    while len(p_list)>0:
        p = p_list.pop(0)

        if (len(stk) == 0) and (p == ')') : 
            stop_flag = True
            print('NO')
            break

        if p == '(' : 
            stk.append(p)
           

        elif p == ')':
            if stk[-1] == '(':
                stk.pop()
               
            else : 
                stk.append(p)
                
    
    if stop_flag : continue

    if len(stk)>0 : 
        print('NO')

    else : 
        print('YES')

    