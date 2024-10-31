import random
import hashlib
import sympy
import math

def generate_params():
    # Generate a prime number p and a generator g
    while not sympy.isprime(p := random.randint(0, 2**7)):
        pass
    g = random.randint(2, p - 1)
    return p, g

def generate_keys(p, g):
    # Generate private key x and public key y
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    return x, y

def H(M):
    # Hash function using SHA-1
    return int(hashlib.sha1(M.encode()).hexdigest(), 16)

# Generate system parameters p and g
p, g = generate_params()
# Generate private and public keys
x, y = generate_keys(p, g)

print("Parameters: p =", p, ", g =", g)
print("Private key (x):", x)
print("Public key (y):", y)

# Message to sign
M = input("Enter the message to sign: ")

# Choose random k that is coprime with p-1
k = random.randint(2, p - 2)
while math.gcd(k, p - 1) != 1:
    k = random.randint(2, p - 2)

# Calculate r and s components of the signature
r = pow(g, k, p)
k_inv = pow(k, -1, p - 1)
s = ((H(M) - x * r) * k_inv) % (p - 1)

print("Signature: (r, s) =", (r, s))

# Signature validation
if not (0 < r < p) or not (0 < s < p - 1):
    print("Invalid signature: r and s out of range")
else:
    # Calculate a and b for verification
    a = pow(g, H(M), p)
    b = (pow(y, r, p) * pow(r, s, p)) % p

    if a == b:
        print("Valid signature")
    else:
        print("Invalid signature")
