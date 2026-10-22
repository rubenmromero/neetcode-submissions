class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.minHeap = []
        heapq.heapify(self.minHeap)

        # Initialize iterator for popping elements from the min-heap
        i = 0

        for num in nums:
            heapq.heappush(self.minHeap, num)

            if len(self.minHeap) > k and i < k:
                heapq.heappop(self.minHeap)
                i += 1

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
            i += 1

        return self.minHeap[0]