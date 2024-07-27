'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
''''
# Code :
class Solution(object):
    def moveZeroes(self, nums):
        temp = []
        cnt = 0
        
        # Separate non-zero elements and count zeroes
        for i in nums:
            if i != 0:
                temp.append(i)
            else:
                cnt += 1

        # Combine non-zero elements and zeroes
        temp2 = [0] * cnt
        
        # Clear the original list and update in-place
        nums[:] = temp + temp2
        return nums
