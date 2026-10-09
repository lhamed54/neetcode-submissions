class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        count = {}
        longest = 0

        for right in range(len(s)):

            # expand window
            count[s[right]] = count.get(s[right], 0) + 1

            # shrink window if invalid
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            # update result
            longest = max(longest, right - left + 1)

        return longest