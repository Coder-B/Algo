# https://leetcode.com/problems/multiply-strings/
from typing import List
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' == num1 or '0' == num2:
            return "0"
        if '1' == num1:
            return num2
        elif "1" == num2:
            return num1
        digSumList,cachedRet = [],dict()
        for i in range(0,len(num2)):
            idx = len(num2) - i - 1
            if '0' ==num2[idx]:
                continue
            else:
                result = ""
                if num2[idx] in cachedRet:
                    result = cachedRet[num2[idx]]
                else:
                    result = self.multiplyOneDigit(num1,num2[idx])
                    cachedRet[num2[idx]] = result
                digSumList.append(result+"0"*i)
        print(digSumList)
        return self.addList(digSumList)
        

    # num2 只有一位
    def multiplyOneDigit(self, num1: str, num2: str) -> str:
        if '0' == num2:
            return "0"
        revertRet,addNum,dig2 = "",0,int(num2)
        len1 = len(num1)
        for idx in range(0,len1):
            dig1 = int(num1[len1-idx-1])
            tmpRes = dig1*dig2+addNum
            addNum = int(tmpRes/10)
            revertRet+=str(tmpRes%10)
        if addNum > 0:
            revertRet+=str(addNum)
        ret = ""
        for i in range(0,len(revertRet)):
            ret+=revertRet[len(revertRet)-i-1]
        return ret

    def addList(self, lists:List[str]) -> str:
        if 0 == len(lists):
            return "0"
        elif 1 == len(lists):
            return lists[0]
        revertSum = ""
        addNum,idx = 0,0
        while True:
            digSum,reachLongest = addNum,True
            for item in lists:
                if idx < len(item):
                    reachLongest = False
                    digSum+=int(item[len(item)-idx-1])
            if reachLongest:
                break
            revertSum+=str(digSum%10)
            addNum = int(digSum/10)
            idx+=1
        if addNum>0:
            revertSum+=str(addNum)
        ret = ""
        for i in range(0,len(revertSum)):
            ret+=revertSum[len(revertSum)-i-1]
        return ret


s=Solution()
# print(s.multiplyOneDigit("123","4"))
print(s.multiply("0", "56"))