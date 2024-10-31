import random
import sympy
import hashlib

def H(M):
    """ Hash function using SHA-256, returns integer representation of hash """
    return int(hashlib.sha256(M.encode()).hexdigest(), 16)

def generate_params():
    # Generate a prime q and a prime p such that p = kq + 1 for some integer k
    q = sympy.nextprime(random.randint(2**4, 2**5))
    while True:
        k = random.randint(2, 50)
        p_candidate = q * k + 1
        if sympy.isprime(p_candidate):
            p = p_candidate
            break
    # Ensure g is a generator of the subgroup of order q
    h = random.randint(2, p - 1)
    g = pow(h, (p - 1) // q, p)  # Proper generator for subgroup of order q
    return p, q, g

def generate_keys(p, q, g):
    # Generate private key x and public key y
    x = random.randint(1, q - 1)
    y = pow(g, x, p)
    return x, y

# Generate system parameters p, q, and g
p, q, g = generate_params()
# Generate private and public keys
x, y = generate_keys(p, q, g)
print("Public key (p, q, g, y):", (p, q, g, y))
print("Private key (x):", x)

# Message to sign
M = input("Enter message: ")

# Choose random k
k = random.randint(1, q - 1)
X = pow(g, k, p)

# Compute e and s for the signature
e = H(M + str(X)) % q
s = (k + x * e) % q
signature = (e, s)
print("Signature (e, s):", signature)

# Signature verification
e, s = signature

# Compute X_d = g^s * y^(-e) mod p, where y^(-e) means modular inverse
y_inv_e = sympy.mod_inverse(pow(y, e, p), p)  # Modular inverse of y^e mod p
X_d = (pow(g, s, p) * y_inv_e) % p

# Compute e_d and verify
e_d = H(M + str(X_d)) % q

# Check if signature is valid
if e == e_d:
    print("Signature is valid")
else:
    print("Invalid signature")
