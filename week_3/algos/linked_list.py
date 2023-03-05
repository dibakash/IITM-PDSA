# python week_2/algos/linked_list.py
class Node:
    def __init__(self, v=None) -> None:
        self.value = v
        self.next = None
        return


class Linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

        return

    def append(self, v):
        new_node = Node(v)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, v):
        new_node = Node(v)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self, index=0):
        if self.head == None:
            return
        elif self.head.next == None:
            popped = self.head.value
            self.head = None
            self.tail = None
            return popped

        key, temp = -1, self.head

        if index == 0:
            popped = self.head.value
            self.head = self.head.next
            return popped
        else:
            while key < index:
                key += 1
                if key + 1 == index:
                    popped = temp.next.value
                    temp.next = temp.next.next
                    return popped

                temp = temp.next

    def __str__(self):
        if self.head == None:
            return ""
        temp = self.head
        res = ""
        while temp.next:
            res += f"{temp.value}, "
            temp = temp.next
            if temp.next == None:
                res += f"{temp.value}"
        return res
