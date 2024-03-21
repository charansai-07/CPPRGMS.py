# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        leftPos  = head
        rightPos = head
        tmp = head
        leftCount = 1
        while tmp:
            if leftCount< k:
                leftCount+=1
                leftPos = leftPos.next
            else:
                if tmp.next:
                    rightPos = rightPos.next
            tmp= tmp.next
        leftPos.val, rightPos.val = rightPos.val, leftPos.val
        return head
