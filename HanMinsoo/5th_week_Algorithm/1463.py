"""
미완
"""
num = int(input())
Array = [0]*(num+1)


for i in range(1,num+1):
    if i == 1:
        Array[i]=0

    elif i==2:
        Array[i]=1

    elif i%3==0 and i%2==0:
        Array[i] = min(Array[int(i/2)]+1, Array[int(i/3)]+1, Array[i-1]+1)

    elif i%3==0:
        Array[i] = min(Array[int(i/3)]+1,Array[i-1]+1)

    elif i%2==0:
        Array[i] = min(Array[int(i/2)]+1,Array[i-1]+1)

    else:
        Array[i] = Array[i-1]+1

print(Array[num])
