class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sent=sentence.split(" ")
        n=len(searchWord)
        for i in range(len(sent)):
            if(len(sent[i])>=n and searchWord==sent[i][:n]):
                return i+1
        return -1