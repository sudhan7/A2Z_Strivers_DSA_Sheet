from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
    
def BFS(node):
    q = deque()
    q.append(node)

    while q :
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

def invert(root):
    if not root:
        return None
    
    temp = root.left
    root.left = root.right
    root.right = temp

    invert(root.left)
    invert(root.right)

    return root
if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(6)
    G = TreeNode(7)

    A.left, A.right = B, C
    B.left, B.right = D, E
    C.left, C.right = F, G
    
    BFS(A)
    print("*********")
    root = invert(A)
    BFS(root)