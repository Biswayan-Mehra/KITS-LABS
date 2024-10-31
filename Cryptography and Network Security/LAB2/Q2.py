#MonoAlphabetic Cipher
import random

print("URK21CS1004")

KeyMap = list(range(1, 27))
random.shuffle(KeyMap)

plainText = "BISWAYAN"

cipherText = ""
for ch in plainText:
   cipherText += chr(KeyMap[ord(ch) - 65] + 64)

outputText = ""
for ch in cipherText:
   outputText += chr(KeyMap.index(ord(ch) - 64) + 65)

print("KeyMap: ", KeyMap)
print("PlainText: " + plainText)
print("CipherText: " + cipherText)
print("PlainText: " + outputText)

"""
KeyMap = [-1] * 26
for idx in range(26):
   rand = math.ceil(random.random() * 26)
   while rand in KeyMap:
      rand = math.ceil(random.random() * 26)

   KeyMap[idx] = rand
"""