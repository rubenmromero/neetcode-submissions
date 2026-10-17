class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            # (l + r) // 2 can lead to overflow
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1