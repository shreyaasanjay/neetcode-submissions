# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        temp = None



        if head == None:
            return None
        #we store curr.next in a temp , then make curr.next = curr.prev and  
        
        while curr:
            #set curr.next to a temp val
            temp = curr.next
            #make the pointer from curr to next node as prev
            curr.next = prev
            #more prev up to curr
            prev = curr
            #set curr to the next node
            curr = temp
        #eventually prev will be the last node as it keeps moving to prev (so returning prev returns everything after)
        return prev


    #so curr is the current node, prev is the node before and 

        
        