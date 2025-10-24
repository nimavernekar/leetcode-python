'''🧩 Problem 5 — Single Number
Prompt
Every element in the list appears twice, except for one element that appears only once.
Find that single element.'''

# Link: https://leetcode.com/problems/single-number/
# Approach: XOR all elements; pairs cancel out, leaving the unique number.

def single(nums):
    result = 0
    for n in nums:
        result ^=n

    return result