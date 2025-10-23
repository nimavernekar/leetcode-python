'''Remove Duplicates from Sorted Array
Modify the array in place so each element appears only once.
Input: [1,1,2,2,3] → Output: [1,2,3]'''

# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Approach: Two-pointer technique

def remove_duplicates(nums):
    if not nums:
        return []
    
    unique = 0

    for i in range(1, len(nums)):
        if nums[i]!=nums[unique]:
            unique+=1
            nums[unique] = nums[i]
    return nums[:unique+1]