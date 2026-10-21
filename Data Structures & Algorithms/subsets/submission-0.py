class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for num in nums:
            # En Python [1, 2] + [3, 4] = [1, 2, 3, 4]
            result += [subset + [num] for subset in result]

        return result