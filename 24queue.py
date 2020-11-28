
"""
from collections import deque
#큐 구현을 위해 deque라이브러리 사용

queue = deque()
#삽입(5-2-3-7) - 삭제() - 삽입(1-4) - 삭제()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)#먼저들어온 순서대로 출력
queue.reverse()
print(queue)
"""

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)