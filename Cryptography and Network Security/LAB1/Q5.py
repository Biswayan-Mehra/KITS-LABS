import random, math

print("URK21CS1004")

plainText = "4f"

key = ""
for _ in range(len(plainText)):
   key += chr((math.ceil(random.random() * 26) + 64))

def encrypt_decrypt(text, key):
   n = len(text)
   outputText = ""
   for idx in range(n):
      outputText += chr(ord(text[idx]) ^ ord(key[idx]))
   return outputText

cipherText = encrypt_decrypt(plainText, key)
outputText = encrypt_decrypt(cipherText, key)

print("PlainText: " + plainText)
print("CipherText: " + cipherText)
print("PlainText: " + outputText)