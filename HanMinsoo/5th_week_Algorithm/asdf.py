"""
미완
"""
how_many = int(input())
list_tree=[]
for i in range(1,how_many+1):
    v1 = list(map(str,input().split()))
    list_tree.append(v1)

A=list_tree[1][0]
start=[A]
visit_pre=[]
visit_inor=[]
visit_post=[]
def preorder(list, start,visit):
    now = start.pop()
    visit_pre.append(now)

    for i in range(1,how_many+1):
        if list_tree[i][0]==now:
            for j in list_tree[now][:0:-1]:
                if list_tree[now][j] != '.':
                    start.append(j)
            preorder(list, start.pop(), visit_pre)
    return visit_pre

#
# def inorder(list,start):
#     pass
#
# def postorder(list,start):
#     pass

preorder(list_tree,start,visit_pre)
# print(inorder(list_tree,A))
# print(postorder(list_tree,A))

