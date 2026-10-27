import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []

        for i in range(0,k):
             heapq.heappush(min_heap, nums[i])

        for i in range(k,len(nums)):
            if (nums[i] <= min_heap[0]):
                continue

            heapq.heappop(min_heap) # pop karo pehle wale element ko
            heapq.heappush(min_heap, nums[i]) # add karo naye element ko
 
        return min_heap[0]

        