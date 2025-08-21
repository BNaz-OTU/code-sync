class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches_stack = sandwiches[::-1]
        count = 0

        while count < len(students):
            # print(f'Student List: {students} | Current Sandwich: {sandwiches_stack[-1]}')
            if (sandwiches_stack[-1] == students[0]):
                sandwiches_stack.pop()
                students.pop(0)
                count = 0
            else:
                temp = students.pop(0)
                students.append(temp)
                count += 1
        
        return len(students)