class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth = k
        self.minHeap = nums

        # Convert the list into a min-heap, which is a specialized
        # tree-based data structure where the parent node is
        # always smaller than or equal to its children)
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.kth:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.kth:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
