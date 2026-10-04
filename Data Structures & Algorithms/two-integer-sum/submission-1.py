class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            nums2=target-nums[i]
            if nums2 not in seen:
                seen[nums[i]]=i
            else:
                return [seen[nums2],i]        