# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #solution with extra space
        #basically construct a blank array and then add elements to that array in the order and then convert that array to a linked list and return the head

        headarray = []
        result = []

        curr = head

        while curr:
            headarray.append(curr.val)
            curr = curr.next
        
        left = 0
        right = len(headarray)-1
        
        while left<right:
            result.append(headarray[left])
            result.append(headarray[right])
            left+=1
            right-=1
            if left==right:
                result.append(headarray[left])
        
        curr = head
        for i in range(len(result)):
            curr.val = result[i]
            curr = curr.next


        
        
        

