class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1=set(nums1)
        nums2=set(nums2)
        list=[]
        for num in nums1:
            if num in nums2:
                list.append(num)
        return list
        