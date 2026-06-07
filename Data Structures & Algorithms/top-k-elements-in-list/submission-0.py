class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = dict()

        for i in nums: # Instantiate dictionary keys
            if i not in dictionary:
                dictionary[i] = 0
            dictionary[i] += 1
        
        return sorted(dictionary, key=dictionary.get, reverse=True)[:k]
