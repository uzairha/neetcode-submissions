class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# Brute Force: Make a first dictionary, and then we store the first 
# words value inside of it, and then if the next one matches it, we 
# can drop it in that one. If it doesnt, we make another dictionary
# which has the values of that one.
# O(n) space

# More optimal solution. We use ONE dictionary, and the key could be the letters inside of the word and the value can be the word itself. We can go through strs and just find all the possible combinations and store them in res before we assign a word to them

        res = {}

        for s in strs:
            count = [0] * 26 # [0,0,0,0......]
        
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)

            if key not in res:
                res[key] = []
            
            res[key].append(s)
    
        return list(res.values())