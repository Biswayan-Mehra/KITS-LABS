import random
import sympy
import math
import hashlib

def H(M):
    return int(hashlib.sha1(M.encode()).hexdigest(), 16)

# Digital Signature Algorithm
def generate_keys():
    while not sympy.isprime(q := random.randint(0, 2**7)):
        pass
    while not sympy.isprime(p := random.randint(0, 2**7)) or (p - 1) % q != 0:
        pass
    h = random.randint(1, p - 1)
    print(h, (p - 1) / q)
    g = int(h**((p - 1) / q))
    x = random.randint(0, q)
    y = int(g**x % p)
    public = (p, q, g, y)
    private = (p, q, g, x)
    return private, public

print("URK21CS1004")
priv, pub = generate_keys()
print("Private key:", priv)
print("Public key:", pub)

M = input("Enter message: ")
p, q, g, x = priv
k = random.randint(1, q - 1)
r = (g**k % p) % q
s = (pow(k, -1, q) * (H(M) + x * r)) % q
sign = (int(r), int(s))
print("Signature is:", sign)

# Verify
p, q, g, y = pub
w = pow(s, -1, q)
u1 = (H(M) * w) % q
u2 = (r * w) % q
v = ((g**u1 * y**u2) % p) % q

if v == r:
    print("Signature verified")
else:
    print("Invalid signature")
