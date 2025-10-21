'''✅ 1️⃣ Move Zeroes to End of List
Input: [0, 1, 0, 3, 12] → Output: [1, 3, 12, 0, 0]
Re-arrange numbers in-place so all zeroes move to the end while keeping non-zero order.'''

# Link: https://leetcode.com/problems/move-zeroes/
# Approach: Two-pointer in-place swap

def move_zeroes(nums):
    non_zero_index = 0  # Pointer for the position of the next non-zero element
    for k in range(len(nums)):
        if nums[k]!=0:
            nums[non_zero_index], nums[k] = nums[k], nums[non_zero_index]
            non_zero_index += 1
    return nums 