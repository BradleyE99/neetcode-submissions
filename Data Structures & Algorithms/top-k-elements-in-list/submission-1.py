class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_map = {}

        for n in nums:
            if n in temp_map:
                temp_map[n] += 1
            else:
                temp_map[n] = 1
        # print(temp_map)
        # items = sorted(list(temp_map.items()), reverse=True)
        values = sorted(list(temp_map.values()), reverse=True)
        # keys = sorted(list(temp_map.keys()))

        # res = []
        # print(items)
        # print(values)
        # print(keys)
        
        # for i, j in items[:k]:
        #     res.append(j)
        # return res
        res = []
        for i in range(k):
            for key, v in temp_map.items():
                if v == values[i]:
                    if key not in res:
                        res.append(key)
                        break
            
            # res.append(temp_map[values[i]])

        return res