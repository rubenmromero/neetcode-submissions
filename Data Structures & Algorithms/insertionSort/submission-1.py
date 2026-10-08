# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Initialize variables
        n = len(pairs)
        result = []

        for i in range(n):
            j = i - 1

            # Move elements that are greater than key one position ahead
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1

            # Clone and save the entire state of the array at this point
            result.append(pairs[:])

        return result
                