from pprint import pprint


class incompatibleMatrices(Exception):
    def __str__(self):
        return "Matrices are not compatible. Check inputs"

    pass


def main():

    a = [
        [1],
        [2],
        [3],
    ]
    b = [
        [1, 3, 4],
    ]

    pprint(matrixMultiply(a, b), width=20)


def matrixMultiply(A, B):
    try:
        if len(A[0]) != len(B):
            raise incompatibleMatrices

        m, n, p = len(A), len(B), len(B[0])

        C = [[0] * p for _ in range(m)]

        for i in range(m):
            for j in range(p):
                for k in range(n):
                    C[i][j] += A[i][k] * B[k][j]

        return C

    except incompatibleMatrices:
        print("matrices are not compatible, check input")


if __name__ == "__main__":
    main()
