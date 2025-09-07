from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        students_queue = deque(students)
        sandwiches_queue = deque(sandwiches)
        rotations = 0  
        while students_queue and sandwiches_queue and rotations < len(students_queue):
            if students_queue[0] == sandwiches_queue[0]:
                students_queue.popleft()
                sandwiches_queue.popleft()
                rotations = 0  
            else:
                students_queue.append(students_queue.popleft())
                rotations += 1
        return len(students_queue)
