#n개의 정수
#연속된 숫자 몇 개를 선택해서 구할 수 있는 합 중 가장 큰 것
a = []
how_many = int(input())
a = list(map(int, input().split()))

stack=[]
plus=0
minus=0
for i in a:
    if i > 0:
        plus += a[i]
        if minus!=0:
            stack.append(minus)
            minus=0

    elif i<0:
        minus+=a[i]

        if plus!=0:
            stack.append(plus)
            plus=0


print(stack)