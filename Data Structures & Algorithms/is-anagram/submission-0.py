class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for n in s:
            freq1[n]=freq1.get(n,0)+1
        for k in t:
            freq2[k]=freq2.get(k,0)+1
        return freq1 == freq2