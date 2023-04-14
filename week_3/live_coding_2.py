"""
A **doubly linked list** is a linked data structure that consists of a set of sequentially linked records called nodes. Each node contains three fields: two link fields (references to the previous and to the next node in the sequence of nodes) and one data field. So, it can be traversed in both directions.

For the given class **doubly_linked_list**, create one methods:

* **insert_at_pos(data,pos):** that accepts an integer `data` and inserts it into the list at given `pos` position where `1 < pos <= length(list)`

**Note-** Use given linked list structure to implementation.

```python
class Node:
    def __init__(self, data):
        self.data = data # Stores data
        self.next = None # Contains the reference of next node
        self.prev = None # Contains the reference of previous node
class doubly_linked_list:
    def __init__(self):
        self.head = None # Contains the reference of first node of the list
        self.last = None # Contains the reference of the last node of the list
```

**Example**

![](linklist.png)

**Sample Input**

```python
[1,3,5,7,9] # Elements for insert in list one by one, start from 1
20 # data
2 # position
```

**Output**

```python
1,20,3,5,7,9 # Traversed list from head to last
9,7,5,3,20,1 # Traversed list from last to head
```

"""


# Prefix Code
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.last = None

    def insert_end(self, data):
        newnode = Node(data)
        newnode.prev = self.last
        if self.head == None:
            self.head = newnode
            self.last = newnode
        else:
            self.last.next = newnode
            self.last = newnode

    # write code here
    # insert_at_pos(data,pos):** that accepts an integer `data` and inserts it into the list at given `pos` position where `1 < pos <= length(list)`
    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        # if first
        if pos == 1:
            if self.head == None:
                self.head = new_node
                self.last = new_node
            else:
                temp = self.head
                new_node.next = temp
                temp.prev = new_node
                self.head= new_node

                # update last pointer
                while temp.next != None:
                    temp = temp.next
                self.last = temp

        else:
            arrow_idx = 1
            temp = self.head

            while arrow_idx < pos - 1:
                temp = temp.next
                arrow_idx += 1

            if temp.next == None:
                temp.next = new_node
                new_node.prev = temp
                self.last = new_node
            else:
                temp.next.prev = new_node
                new_node.next = temp.next
                temp.next = new_node
                new_node.prev = temp



    # Suffix Code

    def traverse(self):
        temp = self.head
        while temp != None:
            if temp.next != None:
                print(temp.data, end=",")
            else:
                print(temp.data)
            temp = temp.next

    def traverse_rev(self):
        temp = self.last
        while temp != None:
            if temp.prev != None:
                print(temp.data, end=",")
            else:
                print(temp.data)
            temp = temp.prev


ins = eval(input())
data = int(input())
pos = int(input())
A = doubly_linked_list()
for i in ins:
    A.insert_end(i)
A.insert_at_pos(data, pos)
A.traverse()
A.traverse_rev()
