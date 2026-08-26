# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #pointers
        if head is None:
            return None
        
        prev = None
        curr = head
        store = None
        while curr:
            Store = curr.next
            curr.next = prev
            prev = curr
            curr = Store
        return prev


        