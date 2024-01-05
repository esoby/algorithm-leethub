class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        my_dict = {}
        
        for stone in stones:
            if stone in my_dict:
                my_dict[stone] += 1
            else:
                my_dict[stone] = 1
        
        cnt = 0
        for jewel in jewels:
            if jewel in my_dict:
                cnt += my_dict[jewel]
        
        return cnt