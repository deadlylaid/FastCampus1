"""
별찍기
입력값이 5일때
*****
 ****
  ***
   **
    *
를 출력하라
"""
star= int(input())

for i in range(star,0,-1):
    print(' '*(star-i)+'*'*i)