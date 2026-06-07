class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a dictionary 

        result = dict()

        for i in strs:
            key = "".join(sorted(i)) # joins sorted array of chars into a str

            if key not in result:
                result[key] = []
            
            result[key].append(i)

        return list(result.values())