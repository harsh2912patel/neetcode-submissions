class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0  # Our main pointer to read the string
        
        while i < len(s):
            j = i
            # Move j forward until it finds the "#" delimiter
            while s[j] != "#":
                j += 1
                
            # Extract the length integer
            length = int(s[i:j])
            
            # Extract the actual word using the length
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            
            # Jump i to the start of the next length prefix
            i = j + 1 + length
            
        return res