"""
주어진 숫자들 중 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""
#how_long = int(input())
list_check=[]
now=0
#list_a=list(map(int,input().split(' ')))
list_a=[1,2,3,4,5,6,7,8,9,10]
print(list_a)
def aa(list_a):
    while list_a:
        now = list_a.pop()
        print(now)
        for t in range(2,now):
            if now%t == 0:
                break
            elif (now-1)==t :
                list_check.append(now)
                break
            elif now%t!=0:
                pass
    return len(list_check)

print(aa(list_a))
