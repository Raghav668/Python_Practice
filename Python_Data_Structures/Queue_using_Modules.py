#collections module -> deque
import collections
deque = collections.deque()
deque.appendleft(10)
deque.appendleft(20)
deque.appendleft(30)
#print(deque)
deque.pop()
#print(deque) #first in first out

#queue module -> class queue
import queue

queue = queue.Queue()
queue.put(10)
queue.put(20)
queue.put(30)
#print(queue.queue)
queue.get()
queue.get()
#print(queue.queue)
queue.get()
#print(queue.queue)
#queue.get(block=False, timeout=1)


#priority queue using list

priority = []
priority.append(1)
priority.append(22)
priority.append(2)
priority.append(12)
priority.sort()
#print(priority)
priority.pop(0)
priority.pop(0)
#print(priority) #FIFO

#priority queue using priority class module
import queue
priority_class = queue.PriorityQueue()
priority_class.put(22)
priority_class.put(1)
priority_class.put(50)
print(priority_class.queue)
priority_class.get()
priority_class.get()
print(priority_class.queue)