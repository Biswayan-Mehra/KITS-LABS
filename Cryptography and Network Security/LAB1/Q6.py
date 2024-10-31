import random

print("URK21CS1004")

plainText = "MEHRA"

key = ""
for _ in range(len(plainText)):
   key += chr((random.randint(1, 26) + 64))

def str2bin(text):
   binText = ""
   for ch in text:
      binText += bin(ord(ch))[2: ].zfill(8)
   return binText

binKey = str2bin(key)
binPlainText = str2bin(plainText)

print("Key       : " + binKey)
print("PlainText : " + binPlainText)

def encrypt_decrypt(text, key):
   outputText = ""
   for idx in range(len(text)):
      outputText += str(int(text[idx]) ^ int(key[idx]))
   return outputText

binCipherText = encrypt_decrypt(binPlainText, binKey)
print("CipherText: " + binCipherText)

def match_bin(text1, text2):
   count = 0
   for idx in range(len(text1)):
      if text1[idx] == text2[idx]:
         count += 1
   return str(count)

print("PlainText vs Key: " + match_bin(binPlainText, binKey))
print("CipherText vs Key: " + match_bin(binCipherText, binKey))
print("PlainText vs CipherText: " + match_bin(binPlainText, binCipherText))