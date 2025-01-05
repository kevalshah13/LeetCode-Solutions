class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        netShifts = [0] * (n + 1)  # One extra for boundary handling

        # Build difference array
        for start, end, direction in shifts:
            shift_val = 1 if direction == 1 else -1
            netShifts[start] += shift_val
            if end + 1 < n:
                netShifts[end + 1] -= shift_val

        # Convert difference array to prefix sum
        current_shift = 0
        for i in range(n):
            current_shift += netShifts[i]
            netShifts[i] = current_shift

        # Build the result using modulo 26 arithmetic
        result_chars = []
        for i in range(n):
            # netShifts[i] might be large or negative, so take % 26
            shift_mod = netShifts[i] % 26

            # Convert s[i] to 0–25 range, add shift, wrap with % 26, and back to ASCII
            original_pos = ord(s[i]) - ord('a')
            new_pos = (original_pos + shift_mod) % 26
            new_char = chr(new_pos + ord('a'))
            result_chars.append(new_char)

        return ''.join(result_chars)



# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
#         netShifts=[0]*len(s)
#         for i in shifts:
#             if(i[2]==1):
#                 for j in range(i[0],i[1]+1):
#                     netShifts[j]+=1
#             else:
#                 for j in range(i[0],i[1]+1):
#                     netShifts[j]-=1
#         print(netShifts)
#         ans=''
#         for i in range(len(s)):
#             new=ord(s[i])+netShifts[i]
#             # print(new)
#             if(new<ord('a')):
#                 ans+=chr(ord('z')-new+ord('a')+1)
#             elif(new>ord('z')):
#                 ans+=chr(ord('a')+new-ord('z')-1)
#             else:
#                 ans+=chr(new) 
#         return ans
        