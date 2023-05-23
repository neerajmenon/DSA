import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        for i, n in enumerate(stones):
            stones[i] = -1 * n
        heapq.heapify(stones)

        while stones and len(stones) > 1:
            g1 = -1 * heapq.heappop(stones)
            g2 = -1 * heapq.heappop(stones)
            res = abs(g1 - g2)
            if res != 0:
                heapq.heappush(stones, -1 * res)

        return -1 * stones[0] if stones else 0