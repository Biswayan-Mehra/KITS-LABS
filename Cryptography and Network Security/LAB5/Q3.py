import random
import sympy

# Global parameters
# Generate a prime number p
while not sympy.isprime(p := random.randint(0, 2**7)):
    pass

# Select g randomly from the range [2, p-1]
g = random.randint(2, p - 1)

# Generate the private key x, a random integer in the range [1, p-1]
x = random.randint(1, p - 1)

# Compute the public key y = g^x mod p
y = pow(g, x, p)

print("URK21CS1004")
print(f"Prime p: {p}, Generator g: {g}")
print("Private and public key:", f"x: {x}, y: {y}")

# Get the message M from the user (must be a number)
M = int(input("Enter message (numeric): "))

# Encryption
# Select a random integer k such that 1 <= k <= p-2
k = random.randint(1, p - 2)

# Compute C1 = g^k mod p
C1 = pow(g, k, p)

# Compute C2 = M * y^k mod p
C2 = (M * pow(y, k, p)) % p

print(f"Ciphertext: C1 = {C1}, C2 = {C2}")

# Decryption
# Compute M = (C1^(p-1-x) * C2) mod p
decrypted_message = (pow(C1, p - 1 - x, p) * C2) % p
print(f"Decrypted message: {decrypted_message}")
