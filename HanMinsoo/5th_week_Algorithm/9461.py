"""
파도반 수열
"""
test_case = int(input())

count = [int(input()) for i in range(1,test_case+1)]

d=[0]*101

d[1]=1
d[2]=1
d[3]=1
d[4]=2
d[5]=2
d[6]=3
d[7]=4
d[8]=5
d[9]=7
d[10]=9


for i in range(11,101):
    d[i]=d[i-1]=d[i-5]

t = int(input())
for i in range(t):
    n = int(input())



