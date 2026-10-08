class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)                   # put all numbers in a set: removes duplicates, and lookups are O(1)
        longest = 0                           # longest run found so far (0 covers the empty-array case)

        for n in num_set:                     # look at each unique number once
            if n - 1 not in num_set:          # if n-1 isn't present, nothing comes before n, so n starts a run
                length = 1                    # the run so far is just n itself
                while n + length in num_set:  # is the next number up (n+1, then n+2, ...) in the set?
                    length += 1               # yes: the run is one longer, check the next one
                longest = max(longest, length)  # run finished: keep it if it beats the previous record

        return longest                        # the length of the longest run found









