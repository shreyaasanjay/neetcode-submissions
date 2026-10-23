# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #ok brain dump
        #so goal is to find the first root where p and q branch off into different subtrees
        #how to check if p and q are in diff subtrees 

        if root == None:
            return None

        if root == p:
            return root
        
        elif root == q:
            return root
        


        left = self.lowestCommonAncestor(root.right, p, q) 
        right = self.lowestCommonAncestor (root.left, p, q)
        
        if left != None and right!= None:
            return root
        
        elif left!=None:
            return left
        
        elif right!=None:
            return right

