class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # Dictionary everything is stored in

        for s in strs: # Getting each word from strs
            count = [0] * 26 # [0,0,0,0......]
        
            for c in s: # Looking at each character in s
                count[ord(c) - ord("a")] += 1 # sub the stuff thats in c into that and it gives you ASCII for the letter you want.
            
            key = tuple(count) # Convert into tuple because we can't have a list as a key

            if key not in res: # Checking if there already is a key for the s we are on
                res[key] = [] # Making a new one if there isn't
            
            res[key].append(s) # Adds the current word to its anagram group
    
        return list(res.values()) # Return only the groups, not the dictionary keys