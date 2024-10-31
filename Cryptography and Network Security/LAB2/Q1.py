#Caesar Cipher
import random

print("URK21CS1004")

plainText = "MEHRA"
key = random.randint(0, 25)

print("Key:", key)

cipherText = ""
for ch in plainText:
   cipherText += chr(((ord(ch) - 65 + key) % 26) + 65)

print("CipherText:", cipherText)

outputText = ""
for ch in cipherText:
   charCode = ord(ch) - 65
   outputText += chr(65 - key + (charCode if charCode >= key else 26 + charCode))

print("OutputText: ", outputText)