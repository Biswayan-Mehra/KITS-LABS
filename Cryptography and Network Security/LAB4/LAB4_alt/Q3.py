from Crypto.Cipher import DES

def pad(text):
   while len(text) % 8 != 0:
      text += ' '
   return text

def des_encrypt(key, text):
   des = DES.new(key, DES.MODE_ECB)
   padded_text = pad(text)
   return des.encrypt(padded_text.encode('utf-8'))

def des_decrypt(key, ciphertext):
   des = DES.new(key, DES.MODE_ECB)
   decrypted_text = des.decrypt(ciphertext).decode('utf-8')
   return decrypted_text.rstrip()

key = b'8bytekey'  # Key must be 8 bytes long
cipher = des_encrypt(key, "I am Biswayan Mehra.")
print("CipherText: ", cipher)
print("PlainText: ", des_decrypt(key, cipher))
