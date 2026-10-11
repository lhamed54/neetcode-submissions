# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #keep iterating, if there is infinite loop there is a cycle
        #but you never get out of the loop so you never know
        #maybe keep an index or copy of the current node?
        #no cycle, index = -1, return false
        curr = head
        index = -1
        arr = set()
        while curr != None:
            if curr in arr:
                return True
            arr.add(curr) 
            curr = curr.next
        return False
