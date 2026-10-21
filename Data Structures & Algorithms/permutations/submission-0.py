class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack([], nums, [False] * len(nums))
        
        return self.result

    def backtrack(self, perm: List[int], nums: List[int], pick: List[bool]):
        if len(perm) == len(nums):
            # perm[:] creates a copy of the list instead of referencing it
            self.result.append(perm[:])
            return

        for i in range(len(nums)):
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                self.backtrack(perm, nums, pick)
                perm.pop()
                pick[i] = False

        