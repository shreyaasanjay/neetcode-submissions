# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #idea is to first check if p and q are null, if btoh are true then yes, and then if one of them is null but the other isnt then false. The check the values and return if true for both left and right subtrees
        if not p and not q:
            return True
        
        if not p and q:
            return False

        if not q and p:
            return False
        
        if q.val != p.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

