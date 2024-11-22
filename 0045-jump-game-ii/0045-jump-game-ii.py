class Solution:
    def jump(self, nums: List[int]) -> int:
        n  = len(nums)
        if n <= 1:
            return 0
        jumps = 0
        farIdx = 0
        farthest = 0
        for i in range(n - 1):
            farthest =  max(farthest, i+nums[i])
            if i == farIdx:
                jumps += 1
                farIdx = farthest

                if farIdx >= n-1:
                    break
        return jumps
