# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head         #first item
        prev = None         # before first item
        while curr:
            nxt = curr.next     #next item
            curr.next = prev    #point back to prev
            prev = curr         #prev is now current item (move forward)
            curr = nxt          #current is now the next item (move forward)
            
        return prev
            
        