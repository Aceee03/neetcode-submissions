class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break
            elif i > 0 and num == nums[i-1]:
                continue

            j = i+1
            k = len(nums) - 1

            while j < k:
                summ = num + nums[j] + nums[k]
                if summ == 0:
                    ans.append([num, nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif summ < 0:
                    j += 1
                else:
                    k -= 1
        return ans    