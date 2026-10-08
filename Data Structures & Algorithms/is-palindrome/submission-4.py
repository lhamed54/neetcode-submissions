class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        left = 0
        right = len(cleaned) - 1
        palindrome = False
        while left < right:
            if cleaned[left].upper() == cleaned[right].upper(): 
                left += 1
                right -= 1
            else:
                return False
        return True
            
