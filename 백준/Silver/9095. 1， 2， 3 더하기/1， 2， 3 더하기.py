n=int(input())

def dp(num):
    d=[0]*12
    d[0]=0
    d[1]=1
    d[2]=2
    d[3]=4

    for i in range(4,num+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]
    
    return d[num]
    
    
for _ in range(n):
    num=int(input())
    print(dp(num))