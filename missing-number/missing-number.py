class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(len(nums)):
            if x == nums[x]:
                continue
            else:
                return x
        return len(nums)