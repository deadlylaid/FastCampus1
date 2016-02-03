"""
BFS와 DFS
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다.
"""

# n,m,v = map(int,input().split())
#
# visited = []#방문체크 하기전용
# stack=[]
# aa=0
# #n은 정점 개수
# #m은 간선 개수
# #v는 탐색을 시작할 정점
# array = [[0 for a in range(n+1)]for b in range(n+1)]
#
# for i in range(m):
#     c, d = map(int,input().split())
#
#     array[c][d]=array[d][c]=1
#
# for i in range(n):
#     visited[i]=0
# #visited =[0 for i in range(n+1)]
#
# while aa == n:#모든 노드를 전부 방문해볼 때까지한다
#     stack.append(v)
#     now = stack.pop()
#     visited[now]=1
#     for p in n:
#         if visited[now]==0 and array[now][p]==1:
#
# n, m, start = map(int, input().split())
# a = [[False for i in range(n+1)] for j in range(n+1)]
# for _ in range(m):
#     u, v = map(int, input().split())
#     a[u][v] = a[v][u] = True
#
# check = [False for i in range(n+1)]
# def dfs(a, check, n, start):
#     stack = [(start, 0)]
#     check[start] = True
#     print(start, end=' ')
#     while stack:
#         now, l = stack[-1]
#         stack.pop()
#         for i in range(l+1, n+1):
#             if a[now][i] and not check[i]:
#                 stack.append((now, i))
#                 print(i, end=' ')
#                 check[i] = True
#                 stack.append((i, 0))
#                 break
#
# dfs(a, check, n, start)
# print()
# check = [False for i in range(n+1)]
# def bfs(a, check, n, start):
#     queue = [start]
#     check[start] = True
#     while queue:
#         now = queue[0]
#         queue = queue[1:]
#         print(now, end=' ')
#         for i in range(1, n+1):
#             if a[now][i] and not check[i]:
#                 queue.append(i)
#                 check[i] = True
# bfs(a, check, n, start)

"""
n, m, start = map(int, input().split())인접한 값 생성
a = [[False for i in range(n+1)] for j in range(n+1)]
for _ in range(m):정점 간의 연결을 다중입력 받기위해 만듦
    u, v = map(int, input().split())
    a[u][v] = a[v][u] = True양방향 연결이기 때문에 두개에 입력

check = [False for i in range(n+1)]방문했는지 안했는지 알기위해서 배열 생성
def dfs(a, check, n정점의 갯수, start):
    stack = [(start, 0)]
    check[start] = True
    print(start, end=' ')
    while stack:
        now, l = stack[-1]
        stack.pop()
        for i in range(l+1, n+1):
            if a[now][i] and not check[i]:
                stack.append((now, i))
                print(i, end=' ')
                check[i] = True
                stack.append((i, 0))
                break

dfs(a, check, n, start)
print()
check = [False for i in range(n+1)]
def bfs(a, check, n, start):
    queue = [start]
    check[start] = True
    while queue:
        now = queue[0]
        queue = queue[1:]
        print(now, end=' ')
        for i in range(1, n+1):
            if a[now][i] and not check[i]:
                queue.append(i)
                check[i] = True
bfs(a, check, n, start)
"""

# ​
# ​
# for _ in range(e):
#     e1, e2 = map(int,input().split())
#     adj[e1][e2] = adj[e2][e1] = 1
# ​
# visited_DFS = [0 for _ in range(v+1)]
# st = [start]
# dfs =[]
# bfs = []
# ​
# while(st):
#     now = st.pop()
# ​
#     if(visited_DFS[now] == 0):
#         dfs.append(now)
#         visited_DFS[now] = 1
# ​
#     for i in range(v, 0, -1):
#         if(adj[now][i] == 1 and visited_DFS[i] == 0):
#             st.append(i)
# ​
# q = [start]
# visited_BFS = [0 for _ in range(v+1)]
# ​
# while(q):
#     now = q.pop(0)
#     if(now == start):
#         visited_BFS[now] = 1
#         bfs.append(now)
# ​
#     for i in range(v+1):
#         if(adj[now][i] == 1 and visited_BFS[i] == 0):
#             q.append(i)
#             visited_BFS[i] = 1
#             bfs.append(i)
# ​
# print(" ".join(map(str, dfs)))
# print(" ".join(map(str, bfs)))
# Add Comment Col
#

#########################
# v, e, start = map(int,input().split())
# #정점의 갯수와 간선의 갯수, 그리고 탐색을 시작하게 될 정점을 input합니다.
#
# #그래프를 표현하기 위해 인접행렬을 만들자
# Array = [[0 for i in range(v+1)]for j in range(v+1)]
# #0번째 인덱스는 안 쓸것이기 때문에 v+1로 해줌
# #print(Array)
#
# for k in range(e):
#     v1 , v2 = map(int,input().split())
#     Array[v1][v2]=Array[v2][v1]=1
#
#     #양방향 인접행렬이기 때문에 양쪽 다 1로 바꿔야 한다.
#
# visited = [0 for x in range(v+1)]
# stack = [start]
# dfs=[]
# while (stack):
#     b=stack.pop()
#     if(visited[b]==0):
#         visited[b]=1
#         dfs.append(b)
#     for i in range(v,0,-1):
#         if Array[b][i]==1 and visited[i]==0:
#             stack.append(i)
# #################
# queue=[start]
# bfs=[]
# visited_1=[0 for z in range(v+1)]
# while (queue):
#     now = queue.pop(0)
#     if (now==start):
#         bfs.append(now)
#         visited_1[now]=1
#     for i in range(1,v+1):
#         if Array[now][i]==1 and visited_1[i]==0:
#             queue.append(i)
#             bfs.append(i)
#             visited_1[i]=1
#
# print(" ".join(map(str, dfs)))
# print(" ".join(map(str, bfs)))

v,e,start=map(int,input().split())

list_ = [[] for i in range(v+1)]
check = [0 for d in range(v+1)]
for i in range(1,e+1):
    v1,v2=map(int,input().split())
    list_[v1].append(v2)
    list_[v2].append(v1)
for t in range(1,v+1):
    list_[t].sort()

def dfs(list_,check,now):
    if check[now]==0:
        check[now]=1
    else:
        return
    print(now,'',end='')
    for z in list_[now]:
        dfs(list_,check,z)

dfs(list_,check, start)
print("")
queue = []
visited_qu=[0 for zz in range(v+1)]


def bfs(list_,check,now):
    queue.append(now)
    while queue:
        now = queue.pop(0)
        visited_qu[now]=1
        print(now,'',end='')
        for my in list_[now]:

            if visited_qu[my]==0:
                queue.append(my)
                visited_qu[my]=1


bfs(list_,check,start)