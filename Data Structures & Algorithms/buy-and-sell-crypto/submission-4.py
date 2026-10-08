class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        curr_sum = 0                        # [10,1,5,6,7,1]
        max_sum = 0                         # [^--^        ] no profit,
                                            # [^---^       ] no profit
                                            # ...
                                            # [^----------^] no profit
                                            # [---^-^      ] profit, current profit, maximum profit

        while right < len(prices):
            if prices[right] > prices[left]:
               curr_sum = prices[right] - prices[left]
               max_sum = max(max_sum, curr_sum)
            else:
                left = right
            right += 1
        return max_sum


