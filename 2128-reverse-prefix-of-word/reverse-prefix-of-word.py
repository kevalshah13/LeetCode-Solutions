class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        flag=0
        for i in range(len(word)):
            if word[i]==ch:
                flag=1
                break
        print(i)
        if flag==1:
            s=word[i::-1]+word[i+1:]
        else:
            s=word
        return s
        # # print(s)
        # return ""