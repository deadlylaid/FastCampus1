how_many = int(input())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

list_A = sorted(A)
list_B = sorted(B,reverse=True)
S = 0
for i in range(how_many):
    S += list_A[i]*list_B[i]

print(S)
