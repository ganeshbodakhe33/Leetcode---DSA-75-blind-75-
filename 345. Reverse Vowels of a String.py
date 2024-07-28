'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''
# Code :
class Solution(object):
    def reverseVowels(self, s):
        chars = list(s)
        vowels = "aeiouAEIOU"
        l = 0
        r = len(s) - 1
        while l<r:
            while l<r and chars[l] not in vowels:
                l += 1
            while l<r and chars[r] not in vowels:
                r -= 1
            # chars[l], chars[r] = chars[r], chars[l]
            temp = chars[l] 
            chars[l] = chars[r]
            chars[r] = temp
            l += 1
            r -= 1
        return ''.join(chars)
