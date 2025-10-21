'''✅ 2️⃣ Check for Duplicates in a List
Input: [1, 2, 3, 1] → Output: True
Return True if any element appears twice in the list.'''


# Link: https://leetcode.com/problems/contains-duplicate/
# Approach: Use a set to track seen numbers

def contains_duplicate(nums):
    seen =set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False