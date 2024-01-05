class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        ans = []
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        
        values_list = list(my_dict.values())
        values_list.sort(reverse=True)
        values_list = values_list[:k]
        
        for num in values_list:
            for key in my_dict.keys():
                print(num, key)
                if num == my_dict[key]:
                    ans.append(key)
                    my_dict[key] = -1

        return ans