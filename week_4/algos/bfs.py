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
    visited, parent = {}, {}
    q = Queue()

    for i in AList.keys():
        visited[i] = False
        parent[i] = -1

    visited[v] = True
    q.enqueue(v)

    while not q.isempty():
        j = q.dequeue()
        for k in AList[j]:
            if not visited[k]:
                visited[k] = True
                parent[k] = j
                q.enqueue(k)
    return visited, parent


AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

print(BFS(AList, 0))
