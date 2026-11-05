class Solution:
    vals = [
        26, 25, 24, 23, 22, 21, 20, 
        19, 18, 17, 16, 15, 14, 13, 12, 11, 10,
        9, 8, 7, 6, 5, 4, 3, 2, 1
    ]
    
    def reverseDegree(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            ret += Solution.vals[ord(s[i]) - 97] * (i + 1)

        return ret
