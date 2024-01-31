class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while(sandwiches and sandwiches[0] in students):
            if students[0]==sandwiches[0]:
                del sandwiches[0]
                del students[0]
            else:
                students.append(students[0])
                del students[0]
        return len(sandwiches)