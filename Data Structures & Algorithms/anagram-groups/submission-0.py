class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = strs
        words = {}
        list_of_lists = []
        for i in strs:
            sort_i = "".join(sorted(i))
            if sort_i not in words:
                words[sort_i] = [i]
            else:
                words[sort_i].append(i)
        for i in words:
            list_of_lists.append(words[i])
        return list_of_lists
            



        