class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        while i < n:
            if n not in nums:
                return n
            if i != nums[i]:
                return i
            i += 1

