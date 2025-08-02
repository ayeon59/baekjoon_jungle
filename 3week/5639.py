#루트노드부터 내려오게 작성

import sys

preorder = []
for line in sys.stdin:
    preorder.append(int(line.strip()))

def set_tree(root,value):
    
tree = {}
for i in range(len(preorder)-1):
    #루트 노드 보다 작은 경우
    root = preorder[i]
    tree[root] = {
        'left': None,
        'right': None
    }
    if preorder[i+1] < root :
        tree[root]['left'] = preorder[i+1]
    else :
        tree[root]['right'] = preorder[i+1] 

print(tree)


# # 트리 구조 저장
# for _ in range(n):
#     root, left, right = input().split()
#     tree[root] = [left, right]


# def preorder(node):
#     if node == '.':
#         return
#     print(node, end='')
#     preorder(tree[node][0])
#     preorder(tree[node][1])


# def inorder(node):
#     if node == '.':
#         return
#     inorder(tree[node][0])
#     print(node, end='')
#     inorder(tree[node][1])


# def postorder(node):
#     if node == '.':
#         return
#     postorder(tree[node][0])
#     postorder(tree[node][1])
#     print(node, end='')

# preorder('A')
# print()
# inorder('A')
# print()
# postorder('A')
