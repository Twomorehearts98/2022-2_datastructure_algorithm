def LCSprint(lst, x, y):
    if lst[x - 1][y - 1] == 0:
        print(A[x-1], end='')
        return
    LCSprint(lst, x - 1, y - 1)
    print(A[x-1], end='')


if __name__ == "__main__":
    A = input("A:")
    B = input("B:")
    LCS = [[0 for i in range(len(B) + 1)] for k in range(len(A) + 1)]
    tmp1 = 0
    tmp2 = 0
    temp = 0
    for n in range(len(A)):
        for m in range(len(B)):
            if A[n] == B[m]:
                LCS[n + 1][m + 1] = LCS[n][m] + 1
                if temp < LCS[n + 1][m + 1]:
                    temp = LCS[n + 1][m + 1]
                    tmp1 = n + 1
                    tmp2 = m + 1
                elif temp == LCS[n+1][m+1]:
                    if(A[tmp1]<A[n]):
                        temp = LCS[n + 1][m + 1]
                        tmp1 = n + 1
                        tmp2 = m + 1
    ans = ""
    length = tmp1
    while temp > 0:
        ans += A[length - 1]
        length -= 1
        temp -= 1
    for i in range(len(ans) - 1, -1, -1):
        print(ans[i], end="")
    print()
    LCSprint(LCS, tmp1, tmp2)
