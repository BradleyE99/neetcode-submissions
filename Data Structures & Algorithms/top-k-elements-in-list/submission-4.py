class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        res = []
        for i, n in enumerate(nums):
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        print(list(d.values()))
        print(d)

        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(d)

        for num in range(k):
            res.append(d[num][0])

        return res

        