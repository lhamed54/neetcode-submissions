# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)  # Starting placeholder
        curr = dummy         # Builds the merged list

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1  # Attach smaller node
                list1 = list1.next # Move list1 forward
            else:
                curr.next = list2  # Attach smaller node
                list2 = list2.next # Move list2 forward

            curr = curr.next       # Move merged-list pointer

        curr.next = list1 or list2 # Attach remaining nodes

        return dummy.next          # Skip placeholder