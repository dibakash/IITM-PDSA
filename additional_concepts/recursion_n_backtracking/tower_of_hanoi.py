# run: python additional_concepts/recursion_n_backtracking/tower_of_hanoi.py

"""
Rules:
only one disk can be moved at a time
never place smaller disk under a larger disk
you can only move a disk from top of a tower
"""


"""
lets the stack towers be like

|1       |       |
|2       |       |
|3       |       |
|4       |       |
|5       |       |

"""
A, B, C = "A", "B", "C"  # towers


def toh(n, A, B, C):
    if n == 0:
        return

    # faith that toh(n-1, A,C,B) and toh(n-1, C, B, A) will follow the rule and run correctly

    toh(n - 1, A, C, B) # move n-1 disk from A to C using B
    print(f"disk{n}: {A}->{B}") # move the largest disk from A to B
    toh(n - 1, C, B, A) # move the n-1 disk from C to B using A


# move 5 disks from A to B (initially using C)
toh(5, A, B, C)
