class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for s in strs:
            sorted_s = ''.join(sorted(s))

            if my_dict.get(sorted_s):
                my_dict[sorted_s] += [s]
            else:
                my_dict[sorted_s] = [s]

        return my_dict.values()