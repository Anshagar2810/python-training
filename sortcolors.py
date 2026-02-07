# Counting Sort Approach
class SolutionCounting:
    def sortColors(self, nums):
        count0 = count1 = count2 = 0

        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        index = 0
        for _ in range(count0):
            nums[index] = 0
            index += 1
        for _ in range(count1):
            nums[index] = 1
            index += 1
        for _ in range(count2):
            nums[index] = 2
            index += 1


# Bubble Sort Approach
class SolutionBubble:
    def sortColors(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]


nums1 = [2, 0, 2, 1, 1, 0]
nums2 = [2, 0, 2, 1, 1, 0]

SolutionCounting().sortColors(nums1)
SolutionBubble().sortColors(nums2)

print("Counting Sort Result:", nums1)
print("Bubble Sort Result:", nums2)