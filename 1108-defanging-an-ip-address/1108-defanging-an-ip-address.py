class Solution:
    def defangIPaddr(self, address: str) -> str:
        list=[]
        for ch in address:
            if ch ==".":
                list.append("[.]")
            else:
                list.append(ch)
        return "".join(list)
        