from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        result= []

        for s in strs:
            sorted_str = tuple(sorted(s))
            anagram_map[sorted_str].append(s)

        for value in anagram_map.values():
            result.append(value)
        return result

        