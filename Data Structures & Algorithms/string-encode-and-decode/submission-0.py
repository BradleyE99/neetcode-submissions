class Solution:

    def encode(self, strs):
        return "".join(str(len(s)) + "#" + s for s in strs)

    def decode(self, s):
        result = []
        i = 0
        while i < len(s):
            # Find the '#' delimiter
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])         # everything between i and j is the number
            result.append(s[j+1:j+1+length])  # grab `length` chars after the '#'
            i = j + 1 + length           # jump to the next encoded string
        return result