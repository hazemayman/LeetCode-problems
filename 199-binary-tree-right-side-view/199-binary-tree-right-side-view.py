# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root == None): return [] 
        nodes = []
        nextNodes = [root]
        values = []
        while(len(nextNodes)):
            nodes = nextNodes
            nextNodes = []
            values.append(nodes[-1].val)
            while(len(nodes)):
                node = nodes.pop(0)
                if(node.left !=None):
                    nextNodes.append(node.left)
                if(node.right != None):
                    nextNodes.append(node.right)
        return values
                
            
        
        