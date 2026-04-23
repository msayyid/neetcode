# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        # count total number of nodes in the list
        count = 0
        curr = head
        while curr: # traverse until we reach the end (None)
            count += 1
            curr = curr.next

        # find the index (0-based) of the node we want to remove
        target = count - n 

        # create a dummy node before head to handle edge cases
        # (removing the first element)
        dummy = ListNode(0)

        # head now is the next of our dummy
        dummy.next = head

        # start from dummy so we can safely remove any node
        curr = dummy

        # move to the node BEFORE the target node
        # after this loop, curr will point to the previous node
        for _ in range(target):
            curr = curr.next
        # now curr = the node before the node we need to remove

        # remove the target node by skipping it
        # link previous node directly to the next node
        curr.next = curr.next.next 

        # return the new head (could be different if head was removed)
        return dummy.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        target = count - n

        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        for _ in range(target):
            curr = curr.next
        curr.next = curr.next.next
        return dummy.next
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node before head
        # this ensures we always have a 'previous' node,
        # even when we need to remove the first element
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # move fast n+1 steps ahead 
        # this creates a gap so that when fast reaches the end,
        # slow will be right before the node we want to remove
        for _ in range(n + 1):
            fast = fast.next


        # now we move both together
        while fast:
            slow = slow.next
            fast = fast.next
            
        # now slow is pointing to the node before the one we want to remove
        # skip the target node
        slow.next = slow.next.next
        
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next