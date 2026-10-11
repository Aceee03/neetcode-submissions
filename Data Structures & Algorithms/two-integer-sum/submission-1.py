class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexes: dict[int, int] = {}

        for i, num in enumerate(nums):
            comp = target - num
            if comp in indexes:
                return [indexes[comp], i]
            indexes[num] = i


        