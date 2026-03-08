# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)


def maxPathSum(root):
    res = [root.val]

    def dfs(root):
        if not root:
            return 0
        
        leftmax = dfs(root.left)
        rightmax = dfs(root.right)
        leftmax = max(leftmax, 0)
        rightmax = max(rightmax, 0)

        res[0] = max(res[0], root.val + leftmax + rightmax)

        return root.val + max(leftmax, rightmax)

    dfs(root)
    return res[0]

A = TreeNode(-15)
B = TreeNode(10)
C = TreeNode(20)
D = TreeNode(15)
E = TreeNode(5)
F = TreeNode(-5)

A.left, A.right = B, C
C.left, C.right = D, E
D.left = F

print(maxPathSum(A))
    