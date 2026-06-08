class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_map = {}

        for c in strs:
            if ''.join(sorted(c)) in temp_map:
                temp_map[''.join(sorted(c))].append(c)
            else:
                temp_map[''.join(sorted(c))] = [c]
        print(temp_map)
   
        return list(temp_map.values())