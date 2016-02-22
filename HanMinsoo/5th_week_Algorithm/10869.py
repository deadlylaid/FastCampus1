"""
두 자연수를 입력했을때
A+B, A-B, A*B, A/B(몫), A%B(나머지)
를 출력하는 프로그램을 작성하라
"""
A, B = map(int, input().split())

print(A+B)
print(A-B)
print(A*B)
print(int(A/B))
print(A%B)