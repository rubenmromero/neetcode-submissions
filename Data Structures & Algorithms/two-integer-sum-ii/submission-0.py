class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            result = numbers[i] + numbers[j]
            if result > target:
                j -= 1
            elif result < target:
                i += 1
            else:
                return [i+1, j+1]