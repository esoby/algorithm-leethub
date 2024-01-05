class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chk = {}

        for item in s:
            if item in chk:
                chk[item] += 1
            else:
                chk[item] = 1

        chklength = len(chk)
        l = list(chk.keys())
        l.sort()

        for idx in range(len(s)):
            tmp = list(s[idx:idx + chklength])
            tmp.sort()
            if ''.join(l) == ''.join(tmp):
                return chklength

        chklength -= 1
        for length in range(chklength, 0, -1):
            for idx in range(len(s)):
                my_str = s[idx : idx + length]
                if len(my_str) < length:
                    break
                
                my_dict = {}
                for ms in my_str:
                    if ms in my_dict:
                        break
                    my_dict[ms] = 1
                print(my_dict)
                if len(my_dict) == length:
                    return length

        return 0