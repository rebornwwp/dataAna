# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution:
    def subsets(self, nums):
        result = []

        def dfs(nums, index, cur, result):
            result.append(cur)
            for i in range(index, len(nums)):
                dfs(nums, i + 1, cur + [nums[i]], result)

        dfs(nums, 0, [], result)

        return result


s = Solution()
print(s.subsets([1, 2, 3]))
