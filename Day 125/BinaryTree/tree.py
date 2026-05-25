class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(node,res = []):
    if node is None:
        return
    
    inorder(node.left,res)
    res.append(node.val)
    inorder(node.right,res)
    return res


def preorder(node,res = []):
    if node is None:
        return
    
    res.append(node.val)
    preorder(node.left,res)
    preorder(node.right,res)
    return res

def postorder(node,res = []):
    if node is None:
        return
    
    postorder(node.left,res)
    postorder(node.right,res)
    res.append(node.val)
    return res

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print("Inorder:  ", inorder(root, []))    
print("Preorder: ", preorder(root, []))   
print("Postorder:", postorder(root, []))
