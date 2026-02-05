class Solution:
    def maxSubArray(self, nums):
        curr_sum = 0
        max_value = nums[0]

        for v in nums:
            curr_sum += v
            max_value = max(max_value, curr_sum)
            if curr_sum < 0:
                curr_sum = 0

        return max_value


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    result = sol.maxSubArray(nums)
    print(result)