class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)

class Codec:

    def serialize(self,root):
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)

    def deserialize(self,data):
        self.i = 0
        vals = data.split(',')

        def dfs():
            if vals[self.i] == "N":
                i+=1
                return None
            
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

def print_tree(node):
    if not node:
        return None
    
    print(node)
    print_tree(node.left)
    print_tree(node.right)

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)

A.left, A.right = B, C
C.left, C.right = D, E

data = (Codec.serialize(A))
print(data)
node = (Codec.deserialize(data))
print_tree(node)
print("*" * 70)
print_tree(A)