# find_all_paths(vertices, gList, source, destination) takes vertices as a list of vertices, gList a dictionary that is an adjacency list for the graph, source is the source vertex and destination is the destination vertex.


def find_all_paths(vertices, gList, source, destination):
    paths = []

    def backtrack(curr, path):
        if curr == destination:
            paths.append(path)
            return

        for neighbor in gList[curr]:
            if neighbor not in path:
                backtrack(neighbor, path + [neighbor])

    backtrack(source, [source])
    return paths


# The function starts by initializing an empty list called paths, which will hold all the paths from source to destination. It then defines a nested function called backtrack that takes two arguments: curr, which represents the current vertex being explored, and path, which is a list of vertices that represents the current path being explored.

# The backtrack function first checks if curr is equal to destination. If so, it appends path to paths and returns. Otherwise, it iterates over all the neighbors of curr in gList. For each neighbor that has not already been visited (i.e., is not already in path), it recursively calls backtrack with the neighbor as the new curr and path + [neighbor] as the new path.

# The backtrack function is initially called with source as curr and [source] as path, since the path starts at the source vertex. After the backtrack function has finished exploring all possible paths from source to destination, it returns the paths list.

# Note that this implementation uses the backtracking technique to explore all possible paths from source to destination. The is_promising function is implicit in the design of the backtrack function, since it only explores paths that have not already visited the current vertex. The generate_candidates function is also implicit, since it iterates over the neighbors of the current vertex in the gList dictionary. The make_move and undo_move functions are not needed in this implementation, since the path variable is passed by value to the recursive calls of the backtrack function.
