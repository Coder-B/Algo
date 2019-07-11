# https://leetcode.com/problems/minimum-window-substring/
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sLen,tLen = len(s),len(t)
        if 0 == sLen or 0 == tLen or sLen < tLen:
            return ""
        tCharMap = dict()
        for c in t:
            if c in tCharMap:    
                tCharMap[c] += 1
            else:
                tCharMap[c] = 1

        low,result,tmpMap,overmap = 0,"",dict(),dict()
        # find first match char
        while low < sLen:
            if s[low] in tCharMap:
                break
            low+=1
        high = low
        for k in tCharMap:
            tmpMap[k] = tCharMap[k]

        while high < sLen:
            if s[high] in tCharMap and s[high] not in tmpMap:
                if s[low] == s[high]:
                    low+=1
                    while low<=high:
                        if s[low] in tCharMap:
                            if s[low] not in overmap:
                                break
                            else:
                                if overmap[s[low]] == 1:
                                    del overmap[s[low]]
                                else:
                                    overmap[s[low]] -= 1
                        low+=1
                else:
                    if s[high] in overmap:
                        overmap[s[high]] += 1
                    else:
                        overmap[s[high]] = 1
            elif s[high] in tCharMap and s[high] in tmpMap:
                if tmpMap[s[high]] == 1:
                    del tmpMap[s[high]]
                    # find one substring
                    if 0 == len(tmpMap):
                        if 0 == len(result) or high-low < len(result):
                            result = s[low:high+1]
                        # slow need ++
                        if s[low] in overmap:
                            if overmap[s[low]] == 1:
                                del overmap[s[low]]
                            else:
                                overmap[s[low]]-=1
                        else:
                            tmpMap[s[low]] = 1
                        low+=1

                        # whether slow need further ++
                        while low <= high:
                            if s[low] in tCharMap:
                                if s[low] not in overmap:
                                    break
                                else:
                                    if overmap[s[low]] == 1:
                                        del overmap[s[low]]
                                    else:
                                        overmap[s[low]] -= 1
                            low+=1
                        print(low)
                else:
                    tmpMap[s[high]]-=1
            high+=1

        return result

s=Solution()
print(s.minWindow("acbbaca","aba"))
