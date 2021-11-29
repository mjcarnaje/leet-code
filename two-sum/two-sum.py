class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMaps = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in previousMaps:
                return [previousMaps[diff], i]
            previousMaps[n] = i
