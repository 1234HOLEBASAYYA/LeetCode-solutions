class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        ans=0
        for ch in operations:
            if ch =="+":
                ans=stack[-1]+stack[-2]
                stack.append(ans)
            elif ch =="D":
                stack.append(2*stack[-1])
            elif ch=="C":
                stack.pop()
            else:
                stack.append(int(ch))
            
        return sum(stack)