def LCS(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    index = L[m][n]
    lcs = [""] * index
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    result = ""
    for char in lcs:
        result += char
    return len(lcs), result

if __name__ == "__main__":
    X = input("Enter the first sequence: ")
    Y = input("Enter the second sequence: ")
    length, sequence = LCS(X, Y)
    print("The length of the Longest Common Subsequence is:", length)
    print("The Longest Common Subsequence is:", sequence)