# temp = map(int,input().split())
# n = temp[0]
# m = temp[1]
v, e = map(int, input().split())

Array = [[0 for i in range(v+1)]for j in range(v+1)]
for k in range(e):
    vv,ii = map(int, input().split())
    Array[vv][ii]=1


for z in Array[1:]:
    print(''.join(map(str,z[1:])))

