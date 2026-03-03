# https://leetcode.com/problems/encode-and-decode-strings/description/
# Time Complexity- O(m) Space Complexity- O(m + n) for encode and decode function calls
# if n = no. of strings, m= no. of chars
class Codec:
    def encode(self, strs: list[str]):
        result = ""
        for char in strs:
            result += str(len(char)) + '#' + char
        return result

    
    # two pointer approach in decode function
    def decode(self, s: str):
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j

        return result


s = Codec()
print(s.decode("5#Hello5#World"))
# print(s.encode(['Hello', 'World']))