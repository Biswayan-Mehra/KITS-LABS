from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# DES requires the key to be exactly 8 bytes
key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)

def des_encrypt(plaintext):
   # Pad plaintext to be multiple of 8 bytes
   padded_text = plaintext + b' ' * (8 - len(plaintext) % 8)
   return cipher.encrypt(padded_text)

def des_decrypt(ciphertext):
   decrypted = cipher.decrypt(ciphertext)
   # Remove padding
   return decrypted.rstrip()

plaintext = b'I am Biswayan Mehra.'  # Must be a multiple of 8 bytes
ciphertext = des_encrypt(plaintext)
print("DES Ciphertext:", ciphertext)

decrypted_text = des_decrypt(ciphertext)
print("DES Decrypted Text:", decrypted_text.decode())
