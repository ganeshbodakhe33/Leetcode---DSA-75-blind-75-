'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has 
its subsequence. In this scenario, how would you change your code?
'''
#------------------------------------------------------------------------------------------------------------------------------------------#
# Code 1 [Optimized]:

class Solution(object):
    def isSubsequence(self, s, t):
        sidx = 0
        tidx = 0
        while(sidx < len(s) and tidx < len(t)):
            if s[sidx] == t[tidx]:
                sidx+=1
            tidx += 1
        if sidx == len(s):
            return True
        else:
            return False
#------------------------------------------------------------------------------------------------------------------------------------------#
# Code 2 [Non optimized]:

class Solution(object):
    def isSubsequence(self, s, t):
        cnt = 0
        for i in s:
            if i in t:
                cnt = cnt + 1
        if cnt == len(s):
            return True
        else:
            return False
#------------------------------------------------------------------------------------------------------------------------------------------#
