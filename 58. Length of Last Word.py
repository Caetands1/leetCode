class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringList = [i for i in s]
        spacesIndex = []
        startAt = -1
        for i in stringList:
            startAt += 1
            if i == " ":
                try:
                    spacesIndex.append(stringList.index(i,startAt))
                except: 
                    spacesIndex.append(stringList.index(i))
        print(spacesIndex)
        return len(''.join(stringList[(spacesIndex[-1]+1):]))


obj = Solution()
print(obj.lengthOfLastWord("   fly me   to   the moon  "))