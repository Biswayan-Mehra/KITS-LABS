from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

print("URK21CS1004")

# Original message
data = "Secrets Messages"
print("Message:", data)

# AES key (must be 16, 24, or 32 bytes long)
key = b'Sixteen byte key'

# Create an AES encryptor object
encryptor = AES.new(key, AES.MODE_ECB)

# Encode the data to bytes
encoded = data.encode()

# Print original encoded length
print("Original length:", len(encoded))
n = len(encoded)

# Padding the data to be a multiple of 16 bytes
if len(encoded) % 16 != 0:
    n = 16 * ((len(encoded) // 16) + 1)
    encoded = pad(data.encode(), n)
    print("Padding to length:", n)
    print("Padded value:", encoded)

# Encrypt the padded data
cipher = encryptor.encrypt(encoded)
print("Encrypted (Base64):", base64.b64encode(cipher).decode("utf-8"))
print("No. of bytes in cipher:", len(cipher))

# Decryption
decryptor = AES.new(key, AES.MODE_ECB)
plaintext = decryptor.decrypt(cipher)

# Unpadding the plaintext if it was padded during encryption
if n % 16 != 0:
    plaintext = unpad(plaintext, n)

# Display the decrypted message
print("Decrypted:", plaintext.decode("utf-8"))
