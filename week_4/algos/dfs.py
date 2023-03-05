# python week_2/algos/dfs.py


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def isempty(self):
        return len(self.stack) == 0

    def Push(self, v):
        self.stack.append(v)
        return self.stack

    def Pop(self):
        if not self.isempty():
            return self.stack.pop()

        return None

    def __str__(self) -> str:
        return str(self.stack)


def DFS(AList, v):
    visited, parent = {}, {}

    for i in AList.keys():
        visited[i] = False
        parent[i] = -1

    s = Stack()
    s.Push(v)

    while not s.isempty():
        j = s.Pop()
        if not visited[j]:
            visited[j] = True

            for k in AList[j][::-1]:
                if not visited[k]:
                    parent[k] = j
                    s.Push(k)

    return visited, parent


AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}

print(DFS(AList, 0))


def DFSInitList(AList):
    visited, parent = {}, {}

    for i in AList.keys():
        visited[i] = False
        parent[i] = -1

    return visited, parent


def DFSRec(AList, visited, parent, v):

    visited[v] = True

    for k in AList[v]:
        if not visited[k]:
            parent[k] = v
        visited, parent = DFSRec(AList, visited, parent, k)

    return visited, parent


AList = {0: [1, 2], 1: [3, 4], 2: [4, 3], 3: [4], 4: []}
v, p = DFSInitList(AList)

print(DFSRec(AList, v, p, 0))
