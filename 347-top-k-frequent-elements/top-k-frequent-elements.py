import heapq
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):
        if self.first != other.first:
            return self.first < other.first

        return self.second < other.second


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = dict()

        # Calculate frequencies
        for i in range(0, len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1

        min_heap = []

        # Go through unique values
        for value in hash_map:
            frequency = hash_map[value]

            heapq.heappush(
                min_heap,
                Pair(frequency, value)
            )

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []

        while min_heap:
            pair = heapq.heappop(min_heap)
            result.append(pair.second)

        return result