from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Key and IV must be 8 bytes long for DES
key = b'8bytekey'  # Key must be exactly 8 bytes
iv = b'8byteIV!'   # IV (Initialization Vector) must be 8 bytes

def des_encrypt(plaintext):
    # Create DES cipher in CBC mode with provided key and IV
    cipher = DES.new(key, DES.MODE_CBC, iv)
    # Pad the plaintext to match the DES block size
    padded_text = pad(plaintext.encode('utf-8'), DES.block_size)
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def des_decrypt(ciphertext):
    # Create DES cipher in CBC mode with provided key and IV for decryption
    cipher = DES.new(key, DES.MODE_CBC, iv)
    # Decrypt the ciphertext and remove padding
    decrypted_padded_text = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded_text, DES.block_size)
    return plaintext.decode('utf-8')

# Example usage:
print("URK21CS1004")

# Original message
message = "Hello it is secret"
print(f"Original message: {message}")

# Encrypt the message
encrypted_message = des_encrypt(message)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = des_decrypt(encrypted_message)
print(f"Decrypted message: {decrypted_message}")
