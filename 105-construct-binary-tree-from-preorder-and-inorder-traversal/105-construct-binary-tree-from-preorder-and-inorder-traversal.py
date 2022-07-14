# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
   
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if (not inorder):
            return None
        
        value = preorder.pop(0)
        Node = TreeNode(value)
        index = inorder.index(value)
        # we pop the first element in preorder as the first element always be the root fot the left subtree
        # here we use the same preorder list across all the function 
        # using the same list in futher functions (limit the memory space)
        Node.left = self.buildTree(preorder,inorder[:index])
        Node.right = self.buildTree(preorder,inorder[index+1:]) 

        return Node