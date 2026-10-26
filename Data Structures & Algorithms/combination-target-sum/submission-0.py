class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        def backtrack(start, current, total):

            if total == target:
                result.append(current.copy())
                return

            if total > target:
                return

            for i in range(start, len(nums)):

                current.append(nums[i])

                backtrack(i, current, total + nums[i])

                current.pop()

        backtrack(0, [], 0)

        return result