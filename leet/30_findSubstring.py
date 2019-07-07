# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
from typing import List
class Solution:
    # Runtime: 372 ms, faster than 56.52% of Python3 online submissions for Substring with Concatenation of All Words.
    # Memory Usage: 13.3 MB, less than 40.76% of Python3 online submissions for Substring with Concatenation of All Words.
    def findSubstring0(self, s: str, words: List[str]) -> List[int]:
        result = []
        if 0 == len(words) or 0 == len(s):
            return result
        constLen,wordsLen,sLen = len(words[0]),len(words),len(s)
        wordsmap = dict()
        for word in words:
            if word in wordsmap:
                wordsmap[word] += 1
            else:
                wordsmap[word]=1
        idx = 0
        tmpMap = dict()
        while idx <= sLen-constLen*wordsLen:
            tmpMap.clear()
            findIdx = True
            for i in range(0,wordsLen):
                startIdx = idx+constLen*i
                seg = s[startIdx:startIdx+constLen]
                print(seg)
                if seg not in wordsmap:
                    findIdx = False
                    break
                else:
                    if seg not in tmpMap:
                        tmpMap[seg] = 1
                    else:
                        if tmpMap[seg] >= wordsmap[seg]:
                            findIdx = False
                            break
                        else:
                            tmpMap[seg]+=1
            if findIdx:
                result.append(idx)
            idx+=1
        return result

# Runtime: 52 ms, faster than 98.67% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 13.2 MB, less than 89.33% of Python3 online submissions for Substring with Concatenation of All Words.
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        if 0 == len(words) or 0 == len(s):
            return result
        constLen,wordsLen,sLen = len(words[0]),len(words),len(s)
        totalLen = constLen * wordsLen
        wordsmap = dict()
        for word in words:
            if word in wordsmap:
                wordsmap[word] += 1
            else:
                wordsmap[word]=1
        idx = 0
        tmpMap = dict()
        for idx in range(0,constLen):
            tmpMap.clear()
            startIdx = idx
            while idx <= sLen-constLen:
                if startIdx > (sLen - totalLen):
                    break
                seg = s[idx:idx+constLen]
                if seg not in wordsmap:
                    tmpMap.clear()
                    startIdx = idx+constLen
                else:
                    if seg not in tmpMap:
                        tmpMap[seg] = 1
                        print("line 68: ",startIdx,s[startIdx:idx+constLen],tmpMap)
                        if idx - startIdx + constLen == totalLen:
                            result.append(startIdx)
                            tmpMap[s[startIdx:startIdx+constLen]]-=1
                            startIdx+=constLen
                            # print(startIdx,s[startIdx:idx+constLen],tmpMap)
                    else:
                        tmpMap[seg]+=1
                        if tmpMap[seg]<=wordsmap[seg]:
                            print("line 77: ",startIdx,s[startIdx:idx+constLen],tmpMap)
                            if idx - startIdx + constLen == totalLen:
                                result.append(startIdx)
                                tmpMap[s[startIdx:startIdx+constLen]]-=1
                                startIdx+=constLen
                                # print(startIdx,s[startIdx:idx+constLen],tmpMap)
                        else:
                            while startIdx<=idx:
                                preSeg = s[startIdx:startIdx+constLen]
                                tmpMap[preSeg]-=1
                                if seg == preSeg:
                                    startIdx+=constLen
                                    break
                                startIdx+=constLen
                idx+=constLen
        return result

s= Solution()
print(s.findSubstring("aaaaaaaa",["aa","aa","aa"]))