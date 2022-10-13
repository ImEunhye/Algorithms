# def solution(brown, yellow):
#     list1 = []
#     count = 0
    
#     for wid in range(3,2500):
#         for hei in range(3,2500):
#             if (wid*hei) == (brown+yellow):
#                 list1.append([wid,hei])
                
#     for li in list1:
#         bro = li[0]*2 + li[1]*2 - 4
#         yel = (li[0]-2) * (li[1]-2)
        
#         if (yel == yellow) and (bro == brown):
#             break
#         count += 1
        
#     if list1[count][0] < list1[count][1]:
#         return [list1[count][1], list1[count][0]]
    
#     return  list1[count]
 
import math
def solution(brown, yellow):
    a = brown + yellow
    li = []
    for i in range(1,a+1) :
        if (a / i) % 1 == 0 :
            li.append(i)
 
    for j in range(math.ceil(len(li)/2)):
        width = max(li[j], li[len(li)-j-1])
        height = min(li[j], li[len(li)-j-1])
   
        brown1 =  width*2 + height*2 - 4
        yellow1 = (width-2) * (height-2)

        if (brown == brown1) and (yellow == yellow1):
            return [width,height]