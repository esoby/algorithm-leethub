from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        nums.sort(key=cmp_to_key(lambda x, y: int(y + x) - int(x + y)))

        return str(int(''.join(nums)))
