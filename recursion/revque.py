#reverse a que
Q = [12,23,34,45,56,67,78,89,90]

# pop element in the queue if there is one 
# else return an empty one

# call reverse queue for remainder

# the push the element to the reversed queueu

from queue import Queue

def Print(queue):
    while (not queue.empty()):
        print(queue.queue[0], end=",")
        queue.get()
        
def revQue(queue):
    Stack = []
    while (not queue.empty()): 
        Stack.append(queue.queue[0])
        queue.get()
    while len(Stack) != 0:
        queue.put(Stack[-1])
        Stack.pop()
        
if __name__ == "__main__":
    queue = Queue()
    queue.put(10)
    queue.put(20)
    queue.put(30)
    queue.put(40)
    queue.put(50)
    queue.put(60)
    queue.put(70)
    queue.put(80)
    queue.put(90)
    revQue(queue)
    Print(queue)