"""
함수의 성격을 반영한다.
하지만 lambda함수는 2줄 이상 쓰는 경우일 거면 그냥
함수를 정의해서 써라
"""
g= lambda x,y:x*y
##위의 람다 함수는
## def g(x,y):
##  return x*y라는 뜻이다 이걸 줄인 것을 람다함수라고 표현한다

print(g(2,3))

h = lambda *args : args*args

print(h(2,5))