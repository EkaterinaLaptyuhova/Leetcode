from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for word in strs:
            w = "".join(sorted(word))
            if w not in d:
                d[w] = [word]
            else:
                d[w].append(word)

        new_list = []
        for key in d:
            temp_list = list(d[key])
            new_list.append(temp_list)
        return new_list


solution = Solution()
print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))