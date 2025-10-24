'''🧩 Problem 3 — Rotate Array
Prompt
Given an array, rotate it to the right by k steps, where k is non-negative.
This means elements move k positions to the right, and the last ones wrap around.
'''

# Problem: Rotate Array
# Link: https://leetcode.com/problems/rotate-array/
# Approach: Slice the array into two parts and rejoin


def array_notes(nums,k):
    k = k % len(nums)

    def reverse (start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)

    return nums


