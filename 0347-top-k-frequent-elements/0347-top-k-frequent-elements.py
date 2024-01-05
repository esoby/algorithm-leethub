class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        
        cnt = sorted(cnt.items(), key=lambda item:item[1], reverse=True)
        
        answer = []
        for i in range(k):
            answer.append(cnt[i][0])
        
        return answer