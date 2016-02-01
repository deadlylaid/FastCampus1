# curser_left=[]
# curser_right=[]
# i=0
# result=''
#
# word = input()#처음 입력되는 값은 무엇인가?
# count = int(input())#몇개의 명령어를 입력할것인가
# for tt in word:
#     curser_left.append(tt)
# while i!=count:
#     order = input()#어떤 명령어를 입력할 것인가?
#     if order.upper()=='L' and len(curser_left)!=0:#L이 나온다면
#         curser_right.append(curser_left.pop())
#     elif order.upper()=='D' and len(curser_right)!=0:
#         curser_left.append(curser_right.pop())
#     elif order.upper()=='B' and len(curser_left)!=0:
#         curser_left.pop()
#     else:
#         a = order.split(' ')
#         if a[0].upper()=='P':
#             curser_left.append(a[1])
#             if len(curser_right)!=0:
#                 asd = curser_right.pop()
#                 curser_left.append(asd)
#
#
#     i+=1
#
# for kk in curser_left:
#     result+=kk
#
#
# print(result)
list_qu =[]
list_result=[]

aef = input()
ttk = aef.split(' ')
how_many = int(ttk[0])
what = int(ttk[1])

a=1
for i in range(1,how_many+1):
    list_qu.append(i)

while list_qu:
    if a%what==0:
        list_result.append(list_qu[0])
        list_qu.pop(0)
    else:
        list_qu.append(list_qu[0])
        del list_qu[0]

    a+=1


li = list(map(str, list_result))
print('<'+", ".join(li)+'>')
