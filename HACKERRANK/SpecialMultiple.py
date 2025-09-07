from collections import deque

def solve(n):
    if n == 0:
        return '0'

    queue = deque()
    queue.append('9')

    visited = set()

    while queue:
        current = queue.popleft()
        remainder = int(current) % n

        if remainder == 0:
            return current

        if remainder not in visited:
            visited.add(remainder)
            queue.append(current + '0')
            queue.append(current + '9')
