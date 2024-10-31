#Vigenère Cipher

print("URK21CS1004")

plainText = "HELLOWORLDIAMBISWAYANMEHRA"

key = "JESUSISTHEANSWER"
i = 0
for _ in range(len(plainText) - len(key)):
   key += key[i]
   i += 1

cipherText = ""
for idx in range(len(plainText)):
   #cipherText += KeyMap[ord(plainText[idx]) - 65][ord(key[idx]) - 65]
   cipherText += chr(65 + ((ord(plainText[idx]) - 65 + ord(key[idx]) - 65) % 26))

outputText = ""
for idx in range(len(cipherText)):
   outputText += chr(65 + ((ord(cipherText[idx]) - ord(key[idx]) + 26) % 26))

print("Key: ", key)
print("PlainText: " + plainText)
print("CipherText: " + cipherText)
print("PlainText: " + outputText)

"""
KeyMap = [[0] * 26 for _ in range(26)]
for row in range(26):
   charCode = chr(65 + row)
   for col in range(26):
      KeyMap[row][col] = charCode
      charCode = chr(((ord(charCode) - 64) % 26) + 65)
"""