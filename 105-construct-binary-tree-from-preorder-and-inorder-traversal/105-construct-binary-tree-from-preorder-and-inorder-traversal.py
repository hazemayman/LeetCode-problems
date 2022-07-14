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
        
        Node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        Node.left = self.buildTree(preorder[1:index+1],inorder[:index])
        Node.right = self.buildTree(preorder[index+1: ],inorder[index+1:]) 

        return Node