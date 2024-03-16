def get_user_input(n):
    list_of_m = []
    values_y=0
    for x in range(1,n):
        values_x = int(input(f"matrix {x} x: "))
        values_y = int(input(f"matrix {x} y: "))
        list_of_m.append(values_x)
    list_of_m.append(values_y)

    return list_of_m

n = int(input("No. of matrices to multiply: "))+1
p = get_user_input(n)
m = array_matrix = [[-1 for _ in range(n+1)] for _ in range(n+1)]
s = array_matrix = [[-1 for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        if(i==j):
            m[i][j] = 0
            s[i][j] = 0


for d in range(1,n):
    for i in range(1,n-d):
        min = 203921023
        j = i+d
        for k in range(i,j):
            q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
            if (q<min):
                min = q
                s[i][j] = k
        m[i][j]=min

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

print_optimal_parens(s, 1, n - 1)