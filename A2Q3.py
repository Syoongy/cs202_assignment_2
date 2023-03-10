import sys


def num_grouping(n, k):
    table = []
    for i in range(n+1):
        table.append([0] * (k+1))

    for i in range(k+1):
        table[i][i] = 1

    for i in range(3, n+1):
        for j in range(3, k+1):
            table[i][j] = table[i-1][j-1] + j * table[i-1][j]

    return table[n][k]


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [int(s) for s in sys.stdin.readline().split()]
    n, k = a[0], a[1]
    print(num_grouping(n, k))
