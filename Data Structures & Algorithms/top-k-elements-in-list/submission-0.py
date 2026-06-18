class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        #frequency of the number
        for num in nums:
            freq[num]=freq.get(num,0)+1
        #sort
        sort_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        result=[]
        #top k elements repeated frequently
        for num,counts in sort_freq[:k]:
            result.append(num)
        return result