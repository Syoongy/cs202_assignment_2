import sys

'''
A)
If k = 1, we can only put all students in 1 group. Therefore, f(n, 1) = 1
If n < k, we cannot split the students into groups such that every group is not empty. Therefore, f(n, k) = 0
If n = k, every student will be in an individual group. Therefore, f(n,k) = 1
If n > k, we have to consider 2 cases:
    Case 1: We put a tripplet into a group by themselves. This leaves us with n-1 students and k-1 groups.
    Therefore, we have f(n-1, k-1) ways to divide the remaining students. Since any of the triplets could be chosen
    to be by themselves, there will be 3 * f(n-1, k-1) ways to divide the students.
    Case 2: We first group every student except for the triplets. This leaves us with n-3 students to divide in
    f(n-3, k) ways. We now can assign each triplet to different groups in 3! = 6 ways. Finally, we can divide the
    remaining students into the 6 * f(n-3, k) possible groups in f(n-3, k) ways. This gives us 6 * f(n-3, k)^2 ways
    to partition the students
Therefore, we have a recurrence relation of: f(n, k) = 6 * f(n-3, k)^2
'''

'''
Total time complexity is O(n*k).
The first loop takes O(n*k) time
The second loop takes O(k) time
The third loop takes O(n*k) time
'''


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
