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
        Node.left = self.buildTree(preorder,inorder[:index])
        Node.right = self.buildTree(preorder,inorder[index+1:]) 

        return Node