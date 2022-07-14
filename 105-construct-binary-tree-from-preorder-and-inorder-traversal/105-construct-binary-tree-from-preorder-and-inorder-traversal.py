# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    lookup = None
    def rec(self, preorder: List[int], inorder: List[int]):
        # rootIndex = self.lookup[preorder[0]]
        rootIndex = inorder.index(preorder[0])
        leftSubTreeInorder   = inorder[:rootIndex]
        rightSubTreeInorder  = inorder[rootIndex+1:]
        leftSubTreepreOrder  = preorder[1:rootIndex+1]
        rightSubTreepreOrder = preorder[rootIndex+1:]
        Node = TreeNode(preorder[0])
        if(len(leftSubTreeInorder)>0):
            left = self.rec(leftSubTreepreOrder,leftSubTreeInorder)
            Node.left = left
        if(len(rightSubTreeInorder)>0):
            right = self.rec(rightSubTreepreOrder,rightSubTreeInorder) 
            Node.right = right
        return Node
               
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.lookup = {inorder[i] : i for i in range(len(inorder))}
        a = self.rec(preorder, inorder)
        return a
            