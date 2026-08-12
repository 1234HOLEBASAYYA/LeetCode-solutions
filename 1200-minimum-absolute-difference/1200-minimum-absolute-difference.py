class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        # diff=99
        mindiff=float('inf')
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            if mindiff>diff:
                mindiff=diff
        ans=[]
        for i in range(len(arr)-1):
            if mindiff==arr[i+1]-arr[i]:
                ans.append([arr[i],arr[i+1]])
        return ans