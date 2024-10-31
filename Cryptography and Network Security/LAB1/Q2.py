print("URK21CS1004")
n = int(input())
m = int(input())
n ^= m
m ^= n
n ^= m
print(n, m)