class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)//2
        major = max(set(nums), key = nums.count)
        count = nums.count(major)

        if count > length:
            return major