# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if(root == None or (root.left == None and root.right == None)):
            return root
        leftBranch = self.flatten(root.left)
        rightBranch = self.flatten(root.right)
        if(leftBranch != None):
            root.right = leftBranch
            while(leftBranch.right != None) : leftBranch = leftBranch.right
            leftBranch.right = rightBranch
        else:
            root.right = rightBranch
        root.left = None
        return root
        
        