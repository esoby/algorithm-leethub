from collections import defaultdict as dict, deque as dq
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char_dict = {}
        # max_length = start = 0

        # for i, char in enumerate(s):
        #     if char in char_dict and start <= char_dict[char]:
        #         start = char_dict[char] + 1
        #     else:
        #         max_length = max(max_length, i - start + 1)

        #     char_dict[char] = i

        # return max_length

        counter = dict(int)
        queue = dq()
        answer = 0
        for char in s:
            counter[char] += 1
            queue.append(char)

            while counter[char] > 1:
                counter[queue.popleft()] -= 1

            answer = max(answer, len(queue))
            
        return answer