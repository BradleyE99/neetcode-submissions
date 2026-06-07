class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []

        for n in range(len(numbers)):
            num_needed = target - numbers[n]

            if num_needed in numbers:
                res.append(n + 1)
                res.append(numbers.index(num_needed) + 1)
                return res
            else:
                continue
        return res