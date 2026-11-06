# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #js for fun i wanna try putting them all in an arry, sorting and then returning index 0, is it bad that this is my intuition LOLL

        arraytree = []


        def treetoarray (root, arraytree):
            if root is None:
                return []
            else:
                arraytree.append(root.val)
            
            treetoarray(root.right, arraytree)
            treetoarray(root.left, arraytree)

            return arraytree

        
        arraytree = treetoarray(root,arraytree)
        if arraytree is not None:
            arraytree.sort()
            print(arraytree)
            return arraytree[k-1]
        return 0
            
