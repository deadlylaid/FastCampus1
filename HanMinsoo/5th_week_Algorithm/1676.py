num = int(input())
sum=1
for i in range(1,num+1):
    sum*=i

sum_str = str(sum)
check_0 = 0
for j in sum_str[::-1]:
    if j =='0':
        check_0+=1
    elif j!='0':
        break

print(check_0)