n = int(input())

ans = ''

def to_binary(n, ans):
    if n <2:
        ans =str(n%2) + ans
        if ans[0] == '0':
            ans = ans[1:]
        return int(ans)
    ans = str(n%2) + ans
    return to_binary(n//2,ans)

print(to_binary(n,ans))

