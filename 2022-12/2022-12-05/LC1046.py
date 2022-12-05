class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones)*(-1)
            x = heapq.heappop(stones)*(-1)

            print(x,y)
            if y != x:
                heapq.heappush(stones,(y-x)*(-1))
        
        if len(stones):
            return stones[0]*(-1)
        else:
            return 0

