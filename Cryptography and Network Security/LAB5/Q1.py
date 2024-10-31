import random
import sympy
import math

def generate_keys():
    # Generate prime p
    while not sympy.isprime(p := random.randint(0, 2**5)):
        pass
    # Generate prime q, ensuring q is not equal to p
    while not sympy.isprime(q := random.randint(0, 2**5)) or p == q:
        pass

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randint(1, phi)
    while math.gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # Calculate d such that (e * d) % phi = 1 (modular inverse of e mod phi)
    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    # Print generated values for debugging
    print(f"Generated values:\n\tp: {p}\n\tq: {q}\n\tn: {n}\n\tphi: {phi}\n\te: {e}\n\td: {d}")

    return private_key, public_key

# Generate keys
priv, pub = generate_keys()

# Output the public and private keys
print("URK21CS1004")
print("Keys:")
print(f"\tPublic: {pub}")
print(f"\tPrivate: {priv}")

# Get user input message to encrypt
M = int(input("Enter message (numeric): "))

# Encrypt the message with the private key (for demonstration purposes)
C = pow(M, priv[0], priv[1])
print("Encrypted:", C)

# Decrypt the message with the public key
decrypted_message = pow(C, pub[0], pub[1])
print("Decrypted:", decrypted_message)
