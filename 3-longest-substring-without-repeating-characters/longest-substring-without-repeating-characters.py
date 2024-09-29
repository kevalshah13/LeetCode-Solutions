class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r=0,0
        ans=0
        mem={}
        for r in range(len(s)):
            # If s[r] is already in the window, shrink from the left
            while s[r] in mem and mem[s[r]] > 0:
                mem[s[l]] -= 1
                if mem[s[l]] == 0:
                    del mem[s[l]]
                l += 1
            
            # Add the current character to the window
            mem[s[r]] = mem.get(s[r], 0) + 1

            # Update the maximum length of the valid window
            ans = max(ans, r - l + 1)
        
        return ans

