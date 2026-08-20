class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = []
        freq = {}
        n = len(grid) * len(grid)

        for row in grid:
            for i in range(len(grid[0])):
                num = row[i]

                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1

        for i in range(1, n + 1):
            if i not in freq:
                l.append(i)

            elif freq[i] == 2:
                l.insert(0, i)

        return l

