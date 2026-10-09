from collections import Counter  # Imports Counter to count how many times each character appears

class Solution:
    def minWindow(self, s: str, t: str) -> str:  # Defines the function; s is the main string and t is the target
        if not s or not t:  # If either string is empty, there cannot be a valid window
            return ""  # Return an empty string

        need = Counter(t)  # Counts the required occurrences of each character in t
        window = {}  # Stores the character counts in the current sliding window

        left = 0  # Left pointer marks the start of the current window
        have = 0  # Counts how many distinct character requirements are currently satisfied
        required = len(need)  # Total number of distinct characters we need to satisfy

        min_len = float("inf")  # Initially sets the shortest valid window length to infinity
        result = ""  # Stores the shortest valid substring found so far

        for right in range(len(s)):  # Moves the right pointer through s, one character at a time
            char = s[right]  # Gets the character at the current right pointer
            window[char] = window.get(char, 0) + 1  # Adds this character to the window's frequency count

            if char in need and window[char] == need[char]:  # Checks whether a required character has just reached its target count
                have += 1  # Marks this character requirement as satisfied

            while have == required:  # Continues shrinking while the window contains all required characters
                if right - left + 1 < min_len:  # Checks whether the current window is shorter than the best one found
                    min_len = right - left + 1  # Updates the shortest window length
                    result = s[left:right + 1]  # Saves the current substring; right + 1 is needed because slicing excludes the end index

                left_char = s[left]  # Gets the character at the left edge of the current window
                window[left_char] -= 1  # Removes one occurrence of that character from the window count

                if (left_char in need  # Checks whether the character being removed is required
                    and window[left_char] < need[left_char]):  # Checks whether removing it leaves too few occurrences
                    have -= 1  # The window is now missing a requirement, so it becomes invalid

                left += 1  # Moves the left pointer forward to shrink the window

        return result  # Returns the shortest valid substring, or "" if none was found
