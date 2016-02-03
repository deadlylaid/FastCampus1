a,p = map(int,input().split())

check = dict()
check[a]=1
cnt =1

def next_number(a,p):
    ans = 0
    while a>0:
        ans +=(a%10)**p
        a//=10
    return ans
while True:
    cnt +=1
    # a-> b
    b = next_number(a,p)
    if b in check:
        print(check[b]-1)
        break
    a=b
    check[a]=cnt

