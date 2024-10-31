def toEncrypt(text, key):
   res = [""] * key
   idx = 0
   step = 1

   for char in text:
      res[idx] += char
      if idx == 0:
         step = 1
      elif idx == key - 1:
         step = -1
      idx += step

   outputText = ""
   for char in res:
      outputText += char
   print(res)
   return outputText

def toDecrypt(text, key):
   outputText = ""

   return outputText

plainText = "GeeksforGeeks"
key = 3

res = [""] * key
idx = 0
step = 1

cipherText = toEncrypt(plainText, key)
print(cipherText)

outputText = toDecrypt(cipherText, key)
print(outputText)