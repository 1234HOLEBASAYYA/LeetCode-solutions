# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        sum=0
        temp=head
        count=0
        while temp!=None:
            temp=temp.next
            count+=1
        count=count-1
        curr=head
        while curr!=None :
            if curr.val==1:
                sum+=2**count
                
            curr=curr.next
            count-=1
        return sum

        