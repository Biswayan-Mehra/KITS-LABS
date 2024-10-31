import random

print("URK21CS1004")

m = int(input())
n = int(input())

hex1 = [[hex(random.randint(1, 100))[2: ].zfill(2) for _ in range(n)] for _ in range(m)]
hex2 = [[hex(random.randint(1, 100))[2: ].zfill(2) for _ in range(n) ] for _ in range(m)]
output = [[-1] * n for _ in range(m)]

for i in range(m):
   for j in range(n):
      output[i][j] = hex(int(hex1[i][j], 16) ^ int(hex2[i][j], 16))[2:].zfill(2)

def PrintHex(hex):
   for i in range(m):
      for j in range(n):
         print(hex[i][j], end=" ")
      print()

print("HEX1: ")
PrintHex(hex1)

print("\nHEX2:")
PrintHex(hex2)

print("\nOUTPUT:")
PrintHex(output)