class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]: return True
        maxDist = 0
        end_index = len(nums)-1
        for i, jump in enumerate(nums):
            if maxDist >= i and i+jump > maxDist:
                maxDist = i+jump
                if maxDist >= end_index:
                    return True
        
        return False
