import random
import sympy

# Global parameters
# Generate a prime number q
while not sympy.isprime(q := random.randint(0, 2**7)):
    pass

# Select a random base 'a' in the range [2, q-1]
a = random.randint(2, q - 1)

# A's private key (xa) and public key (ya)
xa = random.randint(2, q - 1)
ya = pow(a, xa, q)  # ya = a^xa % q

# B's private key (xb) and public key (yb)
xb = random.randint(2, q - 1)
yb = pow(a, xb, q)  # yb = a^xb % q

# Display A's and B's private and public keys
print("URK21CS1004")
print("A's private key and public key:", f"xa: {xa}, ya: {ya}")
print("B's private key and public key:", f"xb: {xb}, yb: {yb}")

# Exchange of public keys and computation of the shared secret
# A computes the shared secret: yb^xa % q
secret_A = pow(yb, xa, q)

# B computes the shared secret: ya^xb % q
secret_B = pow(ya, xb, q)

print("After exchanging public keys, the shared secret is computed as:")
print(f"A's computed secret: {secret_A}")
print(f"B's computed secret: {secret_B}")
