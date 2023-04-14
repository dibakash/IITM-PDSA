"""
A **queue** is a data structure in which whatever comes first will go out first. It follows the FIFO (First-In-First-Out) policy. In Queue, the insertion is done from one end known as the rear end of the queue, whereas the deletion is done from another end known as the front end of the queue.

For a given class **Queue**, create two methods:

* **Enqueue(data):** that accepts an integer `data` and inserts it into the queue in the last position.
* **Dequeue():** if queue is empty, returns `None`. Otherwise, delete one element of the queue from the first position and returns deleted element value.

**Note-**  Use given linked list structure for implementation.

```python
class Node:
    def __init__(self, data):
        self.data = data # store data
        self.next = None #point to the next node
class Queue:
    def __init__(self):
        self.head = None # point to the first node of the list
        self.last = None # point to the last node of the list
```



**Sample input**

```python
[2,4,6,8,10] #elements for insert in queue
3 # remove 3 elements from queue
```

Output

```python
2 # first removed element from queue
4 # second removed element from queue
6 # third removed element from queue
8, 10 #remaining elements in queue
```




"""


# Prefix Code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    # write code here
    def Enqueue(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def Dequeue(self):
        if self.head == None:
            return "None"
        else:
            front = self.head.data
            self.head = self.head.next
            return front

    # Suffix Code

    def traverse(self):
        temp = self.head
        if temp != None:
            while temp != None:
                if temp.next != None:
                    print(temp.data, end=",")
                else:
                    print(temp.data)
                temp = temp.next
        else:
            print("None")


ins = eval(input())
delt = int(input())
A = Queue()
for i in ins:
    A.Enqueue(i)
for j in range(delt):
    print(A.Dequeue())
A.traverse()
