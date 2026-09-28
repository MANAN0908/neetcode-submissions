class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for n in range(len(nums)):
            need = target-nums[n]
            if need in seen:
                return [seen[need], n]
            seen[nums[n]]= n
