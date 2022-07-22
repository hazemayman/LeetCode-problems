# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        curr = root
        while(curr != None):
            if(curr.left == None):
                answer.append(curr.val)
                curr = curr.right
            else:
                pre = curr.left
                while(pre.right != None):
                    pre = pre.right
                pre.right = curr
                temp = curr
                curr = curr.left
                temp.left = None
        return answer
                