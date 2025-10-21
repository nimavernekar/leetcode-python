'''✅ 3️⃣ Maximum Subarray (Sum of Contiguous Elements)
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → Output: 6 (because [4, -1, 2, 1] = 6)
Use Kadane’s Algorithm.'''

# Link: https://leetcode.com/problems/maximum-subarray/
# Approach: Kadane's Algorithm (Dynamic Programming)

def max_sub_array(nums):
    current_sum=max_sum=nums[0]

    for n in nums[1:]:
        current_sum=max(n, current_sum+n)
        max_sum=max(max_sum, current_sum)

    return max_sum