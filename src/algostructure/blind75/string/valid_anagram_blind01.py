"""Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)

        # solution using hashmap is much faster than the sort one
        smap = {}
        tmap = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = 1
            else:
                smap[s[i]] += 1
            if t[i] not in tmap:
                tmap[t[i]] = 1
            else:
                tmap[t[i]] += 1
        for i in s:
            if i not in t:
                return False
            elif smap[i] != tmap[i]:
                return False
        return True

my_result=Solution()
s = "anagram"
t = "nagaram"
print(my_result.isAnagram(s,t))

s = "rat"
t = "car"
print(my_result.isAnagram(s,t))