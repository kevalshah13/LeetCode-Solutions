class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels='aeiou'
        ans=[]
        vowWords=[0]
        countVow=0
        for i in range(len(words)):
            if(words[i][0] in vowels and words[i][-1] in vowels):
                countVow+=1
            vowWords.append(countVow)
        print(vowWords)
        for i,j in queries:
            ans.append(vowWords[j+1]-vowWords[i])
        return ans