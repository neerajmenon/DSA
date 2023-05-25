class MyQueue(object):

    def __init__(self):
        self.stPush = []
        self.stPop = []

    def enq(self, x):
        self.stPush.append(x)
        
    def deq(self):
        self.peek()
        return self.stPop.pop()

    def peek(self):
        if len(self.stPop) == 0:
            while self.stPush:
                self.stPop.append(self.stPush.pop())
        return self.stPop[-1]

    def empty(self):
        return len(self.stPop) + len(self.stPush) == 0
    
    
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    queue_2.append(x)
    while queue_1:
        queue_2.append(queue_1.pop(0))
    queue_1, queue_2 = queue_2, queue_1


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    if queue_1:
        queue_1.pop(0)
