class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = {}
            for i in s:
                if i in count:
                    count[i] += 1
                else:
                    count[i] = 1
            keys = tuple(sorted(count.items()))
            if keys in groups:
                groups[keys].append(s)
            else:
                groups[keys] = [s]
        return list(groups.values())