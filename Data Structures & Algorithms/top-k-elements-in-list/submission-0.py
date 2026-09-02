class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elements = {}

        for i in nums:
            if i in elements:
                elements[i] += 1
            else:
                elements[i] = 1
        
        answer = []

        for x in range(k):
            highest = 0
            for i in elements:
                if elements[i] > highest:
                    highest = elements[i]
                    highest_key = i
            answer.append(highest_key)
            elements.pop(highest_key)
        return answer
                