"""
정수 4를 1, 2, 3의 조합으로 나타내는 방법은 총 7가지가 있다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
정수 n이 주어졌을 때, n을 1,2,3의 합으로 나타내는 방법의 수를
구하는 프로그램을 작성하시오.
"""

how_many = int(input())
b=[0]*11
insert_num=[]
for i in range(1,how_many+1):
    insert_num.append(int(input()))


for a in range(1,11):
    if a == 1:
        b[a]=1
    elif a == 2:
        b[a]=2
    elif a ==3:
        b[a]=4
    else:
        b[a]=b[a-1]+b[a-2]+b[a-3]

for d in insert_num:
    print(b[d])