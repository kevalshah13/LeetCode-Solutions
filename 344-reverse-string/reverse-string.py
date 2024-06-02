class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0,len(s)//2):
            temp=s[i]
            s[i]=s[len(s)-1-i]
            s[len(s)-1-i]=temp
        print(s)

        