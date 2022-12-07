kg = int(input())

def sugar(kg):
    if (kg % 5) == 0:
        return kg//5
    else:
        for j in range(kg//5,0,-1):
            if (kg- 5*j)%3 == 0:
                return j+ (kg- 5*j)//3
        if (kg % 3) == 0:
            return kg//3
    return -1

print(sugar(kg))