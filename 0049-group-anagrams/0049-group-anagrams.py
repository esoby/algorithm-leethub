class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 각 문자열을 정렬한 뒤 비교하는 방식으로 애너그램 여부 확인
        
        # 정렬된 문자열을 key로, 해당되는 애너그램 문자열들의 배열을 value로 관리
        # => k-v 자료구조인 딕셔너리 사용
        my_dict = {}

        for s in strs:
            # 오름차순 정렬된 문자열 = key
            key = ''.join(sorted(s))

            # 해당 key가 딕셔너리에 존재하는지 확인
            if my_dict.get(key):
                # 존재한다면 현재 문자열을 담은 배열을 더해서 저장!
                my_dict[key] += [s]
            else:
                # 존재하지 않는다면 현재 문자열을 담은 배열만 저장!
                my_dict[key] = [s]

        # 딕셔너리의 value 리스트를 뽑아주는 함수 사용
        return my_dict.values()