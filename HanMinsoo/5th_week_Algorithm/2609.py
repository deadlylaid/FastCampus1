# a, b = map(int,input().split())
#
# def gcd(num1, num2):
#     if num2==0:
#         return num1
#     else:
#         return gcd(num2,num1%num2)
#
# def lcm(num1,num2):
#     return int(num1*num2/gcd(a,b))
# print(gcd(a,b))
# print(lcm(a,b))

a,b = map(int,input().split())
check_num =0
def gcd(num1,num2):
    while num2!=0:
        check_num=num1%num2
        num1=num2
        num2=check_num
    return num1

def lcm(num1,num2):
    return num1*num2/gcd(num1,num2)

print(gcd(a,b))
print(lcm(a,b))