"""
별찍기
input = 5 일때
     *
    **
   ***
  ****
 *****
 이 되도록 출력하라
"""
# star = int(input())
#
# for i in range(star):
#     for j in range(star-(i+1),0,-1):
#         print(' ',end='')
#     for p in range(i+1):
#         print('*',end='')
#     print('')



n = int(input())

for i in range(1, n+1):
    print (" " * (n-i) + "*" * i)