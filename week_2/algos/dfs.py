# python week_2/algos/bfs.py


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def isempty(self):
        return len(self.queue) == 0

    def enqueue(self, v):
        self.queue.append(v)
        return self.queue

    def dequeue(self):
        if not self.isempty():
            return self.queue.pop()

        return None

    def __str__(self) -> str:
        return str(self.queue)


def BFS(AList, v):
    level, parent = {}, {}
    q = Queue()

    for i in AList.keys():
        level[i] = -1
        parent[i] = -1

    level[v] = 0
    q.enqueue(v)

    while not q.isempty():
        j = q.dequeue()

        for k in AList[j]:
            if level[k] == -1:
                level[k] = level[j] + 1
                parent[k] = j
                q.enqueue(k)

    return level, parent


AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

print(BFS(AList, 0))
