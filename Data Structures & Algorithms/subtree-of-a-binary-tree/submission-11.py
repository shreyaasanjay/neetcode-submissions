# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        #ok my first instinct is to recurse through the root and once you find
        # a root that is equal to a root in subroot, to check its children against the subroot children 
        #until both are leaves and return true
        # then you do an or statement to check allt he instances where root in root matches root in subroot
        

        #helper function to tell u if a tree starting at root is identical to subroot

        def match(root, subRoot):
            if subRoot is None and root is None:
                return True
            if subRoot is None:
                return False
            if root is None:
                return False
            if root.val != subRoot.val:
                return False
            else:
                return match(root.right, subRoot.right) and match(root.left, subRoot.left)
            
        
        #then check if subroot matches (helper function) root.right or root.left

        if not root and subRoot:
            return False
        if not subRoot:
            return True
        if match(root,subRoot):
            return True            
        else:
            return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)

            