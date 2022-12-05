class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        countWords = Counter(words)
        heap = []
        heapq.heapify(heap)

        for w in countWords.keys():
            heapq.heappush(heap,(countWords[w]*(-1),w))

        res = []
        for _ in range(k):
            _,w = heapq.heappop(heap)
            res.append(w)
        
        return res