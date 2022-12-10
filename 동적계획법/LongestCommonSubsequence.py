def LCSprint(lst, x, y):
    if lst[x - 1][y - 1] == 0:
        print(A[x-1], end='')
        return
    if lst[x][y - 1] == lst[x][y] - 1:
        LCSprint(lst, x - 1, y - 1)
        print(A[x-1], end='')
    else:
        LCSprint(lst, x, y - 1)


if __name__ == "__main__":
    A = input("A:")
    B = input("B:")
    LCS = [[0]*(len(B) + 1) for k in range(len(A) + 1)]
    tmp1 = 0
    tmp2 = 0
    temp = 0
    for n in range(1, len(A) + 1):
        for m in range(1, len(B) + 1):
            if A[n - 1] == B[m - 1]:
                LCS[n][m] = LCS[n - 1][m - 1] + 1
                if temp < LCS[n][m]:
                    temp = LCS[n][m]
                    tmp1 = n
                    tmp2 = m
            else:
                LCS[n][m] = max(LCS[n][m-1], LCS[n-1][m])

LCSprint(LCS, tmp1, tmp2)
