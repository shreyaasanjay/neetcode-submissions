# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #the neetcode submssion without the extra space


        #idea is first reverse the second half of the linked list
        #keep a slow and fast pointer and keep reversing until fast is null or fast.next is null

        if not head:
            return


        prev = None
        #store is storage lol
        store = None


        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next=None

            
        while curr:
            #save the curr's next val
            store = curr.next
            #curr's next pointer is now null 
            curr.next = prev
            #set prev to the current value
            prev = curr
            #move curr up to the next value
            curr = store
        
        #do the merging

        first = head
        #second is the first element of the reversed linked list (second half)
        second = prev

        temp1 = None
        temp2 = None

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2





        













