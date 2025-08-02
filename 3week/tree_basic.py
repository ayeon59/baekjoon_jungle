class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert(current_node.right, value)
    def insert_value(self, value):
        self.insert(self.root, value)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)


bst = BinarySearchTree(1)


n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    