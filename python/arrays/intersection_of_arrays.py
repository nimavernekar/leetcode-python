'''🧩 Problem 4 — Intersection of Two Arrays
Prompt
Given two arrays, return their intersection (unique numbers that appear in both).'''

# Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Approach: Use Python set intersection

'''
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    return list ( set1 & set2)'''


def intersection(nums1, nums2):
    result = []
    for n in nums1:
        if n in nums2 and n not in result:
            result.append(n)
    return result