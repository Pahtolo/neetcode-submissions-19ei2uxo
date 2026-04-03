class Solution:

    def encode(self, strs: List[str]) -> str:
        joined = ""
        for i in strs:
            joined += str(len(i)) + "#" + i
        return joined

    def decode(self, s: str) -> List[str]:
        split = []
        i = 0
        while i < len(s) :
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            i = j+1
            j = i + length
            split.append(s[i:j])
            i = j 

        return split
