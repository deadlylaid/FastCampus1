num = int(input())

if num==0:
    memo=[0]*2
else:
    memo = [0]*(num+1)
def fibo(num):
    memo[0]=0
    memo[1]=1
    if num==0:
        return 0
    elif num==1:
        return 1
    for i in range(2,num+1):
        memo[i]=memo[i-1]+memo[i-2]
    return memo[num]

print(fibo(num))
