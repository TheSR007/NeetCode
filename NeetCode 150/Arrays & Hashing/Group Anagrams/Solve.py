class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        lists = []
        for i in strs:
            isFound = False
            for j in lists:
                if sorted(i) == sorted(j[0]):
                    j.append(i)
                    isFound = True
                    break
            if not isFound:
                lists.append([i])
        return lists