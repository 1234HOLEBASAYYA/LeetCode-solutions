# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        temp=head
        list=[]
        while temp!=None:
            list.append(temp.val)
            temp=temp.next
        s=sorted(list)
        n=len(s)
        temp=head
        for i in range(0,n):
            temp.val=s[i]
            temp=temp.next
        return head

           

