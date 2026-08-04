# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        temp=head
        while temp:
           
            if temp.val==val:
                pre.next=temp.next
                temp=temp.next
            else:
                pre=temp
                temp=temp.next
            
        return dummy.next
            