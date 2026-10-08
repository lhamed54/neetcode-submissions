class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_s = sorted(s)
        char_t = sorted(t)
        return char_s == char_t