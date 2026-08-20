class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        slow = 0
        fast = len(people) - 1
        count = 0

        while slow <= fast:

            if people[slow] + people[fast] <= limit:
                slow += 1

            fast -= 1
            count += 1

        return count