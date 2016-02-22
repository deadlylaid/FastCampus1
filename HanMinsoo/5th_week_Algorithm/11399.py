num = int(input())

list_a = list(map(int, input().split()))

do_sort = sorted(list_a)
sum = 0
sum_list=[]
for index,value in enumerate(do_sort):
    if index+1==1:
        sum_list.append(value)
    else:
        value = value+sum_list[index-1]
        sum_list.append(value)
for value2 in sum_list:
    sum+=value2

print(sum)

