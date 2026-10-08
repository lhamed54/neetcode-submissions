class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = set()
        longest = 0
        while right in range(len(s)):
            if s[right] not in window:
                window.add(s[right])
                longest = max(longest, len(window))
                right += 1
            else:
                window.remove(s[left])
                left += 1
        print(window)
        return longest
        