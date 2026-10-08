class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortlist = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left < right:
            if sortlist[left] + sortlist[right] > target:
                right -= 1
            elif sortlist[left] + sortlist[right] < target:
                left += 1
            else:
                a = sortlist[left]
                b = sortlist[right]
                i = nums.index(a)
                j = nums.index(b, i + 1) if a == b else nums.index(b)
                return [min(i, j), max(i, j)]