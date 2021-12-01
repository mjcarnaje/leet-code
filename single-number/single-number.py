class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps = {}
        for x in nums:
            if x in maps:
                maps[x] = False
            else:
                maps[x] = True
        return list(maps.keys())[list(maps.values()).index(True)]
