class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        disappeared_nums = []

        for i, n in enumerate(nums):
            if n > 0:
                disappeared_nums.append(i + 1)

        return disappeared_nums