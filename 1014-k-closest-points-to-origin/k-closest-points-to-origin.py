import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = []

        for i in range(0, len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            distance = ((x1) ** 2 + (y1) ** 2) ** 0.5
            heapq.heappush(min_heap, (distance, x1, y1)) # storing the distances with points 

        result = []
        for i in range(0, k):
            distance, x1, y1 = heapq.heappop(min_heap) # we are poping the min element from the heap
            result.append([x1, y1])

        return result



            