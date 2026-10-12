# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find/get to tail
        #go back n times (so curr is n)
        #.remove curr
        #return head

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
        
        '''
        while curr:
            nxt = curr.next
            curr = nxt
        tail.next = curr
        while curr:
            for i in range(n):
                curr.next = tail
                nxt = tail.next
                tail = nxt
                curr = tail
            curr.remove
        return head
        '''