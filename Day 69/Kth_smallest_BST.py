# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    n = 0
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        n += 1
        if n == k:
            return curr.val
        curr = curr.right


A = TreeNode(4)
B = TreeNode(3)
C = TreeNode(5)
D = TreeNode(2)

A.left, A.right = B, C
B.left = D

print(kthSmallest(A,4))

