a = int(input())
ans = [0]

for i in range(1,a+1):
    if i == 1:
        ans.append(1)

    elif i == 2:
        ans.append(2)

    else:
        ans.append(ans[i-1]+ans[i-2])


print(ans[a]%10007)