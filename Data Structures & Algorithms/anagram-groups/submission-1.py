class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #if we can count the occurrences of each letter in each word and then group the ones with the same counts

        anagrams_dict = defaultdict(list)

        for i in strs:
            key = "".join(sorted(i))
            anagrams_dict[key].append(i)

        return list(anagrams_dict.values())

