# https://leetcode.com/problems/integer-to-roman/
class Solution:
    grades = ["I", "V", "X", "L", "C", "D", "M"]
    def intToRoman(self, num: int) -> str:
        res = ""
        i,divide = 0,10
        while num > 0:
            residue = int(num % divide)
            res = self.convert(i,residue)+res
            i += 1
            num = int(num/divide)
        return res

    def convert(self, i:int, residue:int) -> str:
        baseIdx = 2*i
        ret = ""
        if residue <= 3:
            ret = self.grades[baseIdx]*residue
        elif residue <= 5:
            ret = self.grades[baseIdx]*(5-residue) + self.grades[baseIdx+1]
        elif residue <= 8:
            ret = self.grades[baseIdx+1] + self.grades[baseIdx]*(residue-5)
        else:
            ret = self.grades[baseIdx]+self.grades[baseIdx+2]
        return ret

s=Solution()
print(s.intToRoman(20))
