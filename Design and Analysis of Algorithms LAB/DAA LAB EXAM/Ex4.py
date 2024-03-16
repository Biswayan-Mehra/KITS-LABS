str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

LCS = [[0]*(len(str1)+1) for _ in range(len(str2)+1)]
length = 0

for i in range(len(LCS)):
    for j in range(len(LCS[i])):
        if i == 0 or j == 0:
            LCS[i][j]=0
        elif str2[i-1] == str1[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
        length = LCS[i][j]

print("Length: ", length)

for i in range(len(LCS)):
    for j in range(len(LCS[i])):
        print(LCS[i][j],end=" ")
    print()

n = len(str2)
m = len(str1)

index = LCS[n][m]

str = [""]*index

while n > 0 and m > 0:
    if str2[n-1] == str1[m-1]:
        str[index-1] = str2[n-1]
        n -= 1
        m -= 1
        index -= 1
    elif LCS[n-1][m] < LCS[n][m-1]:
        m -= 1
    else:
        n -= 1
    
for ch in str:
    print(ch,end="")
              

"""
AGGTAB
GXTXAYB
"""