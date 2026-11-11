import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (smaller half, negative numbers)
        self.large = []  # Min heap (larger half, positive numbers)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)  # Add number to max heap
        heapq.heappush(self.large, -heapq.heappop(self.small))  # Move largest from small to large
        if len(self.large) > len(self.small):  # Check if large has more elements
            heapq.heappush(self.small, -heapq.heappop(self.large))  # Move smallest from large back to small

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):  # Odd number of elements
            return -self.small[0]  # Return middle element
        return (-self.small[0] + self.large[0]) / 2  # Even number: average the two middle elements
