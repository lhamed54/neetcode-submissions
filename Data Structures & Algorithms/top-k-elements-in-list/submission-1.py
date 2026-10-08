class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counts = Counter(nums)
        top = counts.most_common(k)
        return [num for num, count in top]

