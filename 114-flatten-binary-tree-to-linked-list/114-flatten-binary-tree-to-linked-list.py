# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if(root == None or (root.left == None and root.right == None)):
            return [root,root]
        leftBranchNodes = self.flatten(root.left)
        rightBranchNodes = self.flatten(root.right)
        if(leftBranchNodes[0] != None):
            root.right = leftBranchNodes[0]
            leftBranchNodes[1].right = rightBranchNodes[0]
        else:
            root.right = rightBranchNodes[0]
        root.left = None
        
        print(root.val," - " , rightBranchNodes[1])
        print()
        
        return [root ,rightBranchNodes[1] if rightBranchNodes[1] else leftBranchNodes[1]]
        
        