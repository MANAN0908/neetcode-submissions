class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result=[]
        for n in nums:
            freq[n]=freq.get(n,0)+1
        pairs=list(freq.items())
        pairs.sort(key=lambda x:x[1],reverse=True)
        for num,count in pairs[:k]:
            result.append(num)
        return result

        