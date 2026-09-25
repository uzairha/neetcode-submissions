class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]for i in range(len(nums) + 1)] # Makes a list that has 7 [] inside of it. 6 + 1 so itll be 0 - 6 THE BUCKET

        for n in nums: # Looping through each value in nums
            count[n] = 1 + count.get(n, 0) # Adds 1 to everytime we have seen it in the dictionary and if its not there its a 0.
        for n, c in count.items(): # Look at the updated count, and look at the n, and the c that is with it.
        # n is the number and c is how many times it appeared.
            freq[c].append(n) # Update freq aka the bucket with the values from count. So if we saw 1 : 3 times it would save 1 in the 3 bucket.

        res = [] # Make a list for the result

        for i in range(len(freq) -1, 0, -1): # Loop through the whole freq list from the back and go -1 each time
            for n in freq[i]: # Loop through every number stored in the current bucket
                res.append(n) # Add that number to the result
                if len(res) == k: # If length of res = k 
                    return res # You're done

