from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(key, text):
   cipher = AES.new(key, AES.MODE_ECB)
   ciphertext = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
   return ciphertext

def aes_decrypt(key, ciphertext):
   cipher = AES.new(key, AES.MODE_ECB)
   plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')
   return plaintext

key = b'16byteaeskey1234'  # Key must be 16 bytes long
ciphertext = aes_encrypt(key, "I am Biswayan Mehra.")
print("CipherText: ", ciphertext)
print("PlainText: ", aes_decrypt(key, ciphertext))
