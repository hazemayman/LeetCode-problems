# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    solution = []
    def rec (self , root):
        if(root == None) : return []
        if(root.left != None): self.rec(root.left)
        self.solution.append(root.val)
        if(root.right != None): self.rec(root.right)
        return self.solution
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.solution = []
        answer = self.rec(root)
        return answer
        