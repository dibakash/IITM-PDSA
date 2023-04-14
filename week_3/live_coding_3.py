"""
Implement a Stack using only two Queues. The implemented Stack should support all the functions of a normal stack (`push`, `pop`, `top`, and `isempty`).

Create the following method for given class `stack`.

- `push(data)` insert element `data` to the top of the stack.
- `pop()` If stack is empty return message `Stack is empty`. Otherwise, remove the element from the top of the stack and return it.
- `top()` If stack is empty return message `Stack is empty`. Otherwise, return the element on the top of the stack.
- `isempty()` Returns `True` if the stack is empty, `False` otherwise.

**Sample Input**

```
[10,20,30,40,50] #push one by one
2 # pop 2 elemnts
```

**Sample Output**

```
50 #first popped element
40 #second popped element
30 #top element
False #isempty
```

"""
# Prefix Code
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, key):
        self.items.insert(0, key)

    def dequeue(self):
        return self.items.pop()

    # 1,2,3,4
    # 1 [4,3,2,1]
    # 2 []


class stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.size = 0

    # Write code here

    # `isempty()` Returns `True` if the stack is empty, `False` otherwise.
    def isempty(self):
        return self.size == 0

    # `push(data)` insert element `data` to the top of the stack.
    def push(self, data):
        self.q1.enqueue(data)
        self.size += 1

    # `pop()` If stack is empty return message `Stack is empty`. Otherwise, remove the element from the top of the stack and return it.
    def pop(self):
        if self.isempty():
            return "Stack is empty"

        while self.q1.items:
            item = self.q1.dequeue()
            if self.q1.items:
                self.q2.enqueue(item)
        self.q1, self.q2 = self.q2, self.q1
        self.size -= 1
        return item

    # `top()` If stack is empty return message `Stack is empty`. Otherwise, return the element on the top of the stack.
    def top(self):
        if self.size == 0:
            return "Stack is empty"
        item = self.pop()
        self.push(item)
        return item


# Suffix Code
inp = eval(input())
dl = int(input())
A = stack()
for el in inp:
    A.push(el)
for i in range(dl):
    print(A.pop())
print(A.top())
print(A.isempty())
