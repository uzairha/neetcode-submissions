class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            count = [0] * 26

            for c in s:
                nums = ord(c) - ord("a")
                count[nums] += 1

            my_count = tuple(count)

            if my_count in groups:
                groups[my_count].append(s)
            else:
                groups[my_count] = [s]

        return list(groups.values())