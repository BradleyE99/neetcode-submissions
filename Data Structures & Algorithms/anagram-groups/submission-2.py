class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        # Key: the anagram (sorted)
        # Value: the array contianing each version of anagram contianed in strs


        for i, word in enumerate(strs):
            curr_sorted_word = "".join(sorted(word))
            if curr_sorted_word in d:
                d[curr_sorted_word].append(word)
            else:
                d[curr_sorted_word] = [word]
        return list(d.values())
