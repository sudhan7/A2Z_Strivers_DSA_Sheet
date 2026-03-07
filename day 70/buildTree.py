class TreeNode:
    def __init__(self,val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

def DFS(root):
    if not root:
        return None
    
    print(root)
    DFS(root.left)
    DFS(root.right)


def buildTree(preorder,inorder):
    if not preorder or not inorder:
        return None
    
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root

preorder = [1,2,3,4]
inorder = [2,1,3,4]
root  = buildTree(preorder,inorder)
DFS(root)