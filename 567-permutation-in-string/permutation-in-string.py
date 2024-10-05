class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        
        countS1 = Counter(s1)
        countS2 = Counter()
        
        l = 0
        matches = 0
        for r in range(len(s2)):
            # Add the current character to the sliding window count
            countS2[s2[r]] += 1
            
            # Check if the current character in the window matches the count in s1
            if s2[r] in countS1 and countS2[s2[r]] == countS1[s2[r]]:
                matches += 1
            
            # If the window is too large, remove the leftmost character
            if r >= len(s1):
                left_char = s2[l]
                if left_char in countS1:
                    if countS2[left_char] == countS1[left_char]:
                        matches -= 1
                    countS2[left_char] -= 1
                l += 1
            
            # Check if the current window matches the length of s1 and has all the characters
            if matches == len(countS1):
                return True
        
        return False
