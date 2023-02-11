#collection Module
#deque Module
import collections
stack_deque = collections.deque()
stack_deque.append(1)
stack_deque.append(2)
stack_deque.append(3)
print(stack_deque)
stack_deque.pop() #LIFO
print(stack_deque)
stack_deque.pop()
print(stack_deque)

#queue Module-> LIFOqueues

import queue
stack_queue = queue.LifoQueue(5)
stack_queue.put(22)
stack_queue.put(33)
stack_queue.put(44)
stack_queue.put(55)
stack_queue.put(66)
print(stack_queue.queue)
stack_queue.get()
stack_queue.get()
print(stack_queue.queue)
