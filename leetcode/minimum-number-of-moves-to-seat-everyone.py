class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        count = 0

        for idx in range(len(students)):
            count += abs(seats[idx] - students[idx])
        
        return count