class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        cache = {}
        
        for key, score in items:
            heap = cache.get(key, [])
            heap.append(score)
            heapq.heapify(heap)
            while len(heap) > 5:
                heapq.heappop(heap)
            cache[key] = heap

        res = []
        for key, scores in cache.items():
            avg = sum(scores) // 5
            res.append([key, avg])
        res.sort(key=lambda x: x[0])
        return res
