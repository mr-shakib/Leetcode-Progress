class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        sorted_nums = sorted(nums)
        for n in range(len(sorted_nums) - 1):
            if sorted_nums[n] == sorted_nums[n+1]:
                return True
        return False