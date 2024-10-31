#Affine Cipher

print("URK21CS1004")

plainText = "TWENTYFIFTEEN"
a = int(input())
b = int(input())

cipherText = ""
for ch in plainText:
   cipherText += chr(((a * (ord(ch) - 65) + b) % 26) + 65)

mod_inverse = pow(a, -1, 26)

outputText = ""
for ch in cipherText:
   outputText += chr(((mod_inverse * (ord(ch) - 65 - b)) % 26) + 65)

print("PlainText: " + plainText)
print("CipherText: " + cipherText)
print("PlainText: " + outputText)

"""
Decryption Brute-Force Method:
outputText = ""
for ch in cipherText:
   charCode = (ord(ch) - 65)
   for i in range(26):
      if ((26 * i) + charCode - b) % a == 0:
         charCode = ((26 * i) + charCode - b) // a
         break
"""