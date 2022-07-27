# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if(root == None or (root.left == None and root.right == None)):
            # if the root is None , or doesn't have a righ and child nodes return 
            # it as the first and last node in that branch 
            return [root,root] 
        
        leftBranchNodes = self.flatten(root.left) # flat the left branch of the root
        rightBranchNodes = self.flatten(root.right) # flat the right branch of the root
        if(leftBranchNodes[0] != None): # if the left branch existed 
            root.right = leftBranchNodes[0] # make the right child of the root is the first Node in the flattened left branch
            leftBranchNodes[1].right = rightBranchNodes[0] # make the right of the last Node in the flattened left branch 
                                                           # is the first Node in the flattened right branch 
        else:
            root.right = rightBranchNodes[0] # if the root doesn't have a left branch , make the right child points to the first
                                             # Node in the flattened right branch
        root.left = None 
        
#         print(root.val," - " , rightBranchNodes[1])
#         print()
    
        # return the root - first Node in the flattened branch - and the last Node of the flattened branch 
        # which is equal to the last Node in the right branch if existed otherwise will be the last Node
        # in the left branch 
        return [root ,rightBranchNodes[1] if rightBranchNodes[1] else leftBranchNodes[1]] 
    
        
        