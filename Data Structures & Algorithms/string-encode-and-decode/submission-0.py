class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for item in strs:
            encoded += str(len(item)) + ":" + item
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        length_start = 0

        while i < len(s):
            while s[i] != ":":
                i += 1
            
            length = int(s[length_start:i])
                
            start = i + 1
            stop = i + length + 1
            
            word = s[start:stop]
            decoded.append(word)
            i = stop
            length_start = stop
        return decoded


            
