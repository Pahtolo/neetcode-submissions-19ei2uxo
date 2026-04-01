class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no_dupes = sorted(set(nums))
        if not no_dupes:
            return 0
        if len(no_dupes) == 1:
            return 1
        temp_list = [no_dupes[0]]
        return_list = [no_dupes[0]]
        for i in range(1, len(no_dupes)):
            if no_dupes[i] == no_dupes[i-1] + 1:
                temp_list.append(no_dupes[i])
                if len(temp_list) > len(return_list):
                    return_list = temp_list
            else:
                temp_list = []
                temp_list.append(no_dupes[i])
        return len(return_list)
            

            
        