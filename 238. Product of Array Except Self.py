'''
238. Product of Array Except Self
Attempted
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i].The product of any prefix or suffix of nums is 
guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
'''
#-------------------------------------------------------------------------------------------------------#
# Code 1 [Optimized]:
class Solution(object):
    def productExceptSelf(self, nums):
        length = len(nums)
        # Initialize the result array with 1s
        result = [1] * length
        
        # Compute prefix products
        prefix = 1
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]
        
        # Compute suffix products and finalize the result
        suffix = 1
        for i in range(length - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
#-------------------------------------------------------------------------------------------------------#
# Code 2 [Not Optimized]:
class Solution(object):
    def productExceptSelf(self, nums):
        result = []
        length = len(nums)
        for i in range(length):
            product = 1
            for j in range(length):
                if i != j:
                    product *= nums[j]
            result.append(product)
        
        return result
#-------------------------------------------------------------------------------------------------------#
