'''Prompt
ou are given an array containing n distinct numbers taken from 0, 1, 2, …, n.
Return the missing number.
'''
# Link: https://leetcode.com/problems/missing-number/
# Approach: Math formula (sum of 0..n) - actual sum


def missing_number(nums):
    n= len(nums)
    expected_sum = n+(n*(n-1))//2
    actual_sum = sum(nums)
    return expected_sum - actual_sum