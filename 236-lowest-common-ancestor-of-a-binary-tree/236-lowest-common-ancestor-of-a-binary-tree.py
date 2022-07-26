# Definition for a binary tree node.
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # if the root is the node we are trying to find (q or p) then return it 
        # if the root is None that means this branch doesn't have p or q and therfore we return None 
        if(root == p or root == q or root == None): return root
        left = self.lowestCommonAncestor(root.left , p , q) # traverse to find q or p
        right = self.lowestCommonAncestor(root.right , p , q) # traverse to find q or p 
        
        if(left and right): return root # if left branch of this node found a node as well as the right brancg 
                                        # then that means p and q is in separate branches from the this root node 
                                        # return this root node as the LCA
                
        return left if left else right  # if one of the branches is empty that means one of them is the parent of the other
                                        # return the not None Node as the LCA
                