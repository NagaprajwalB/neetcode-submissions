class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        n = len(nums)
        for i in range(n-1 ,-1,-1):
            if nums[i] == val:
                del nums[i]
        res = len(nums)
        return res