def RC4(key, text):
   S = list(range(256))
   j = 0
   key = [ord(c) for c in key]

   # KSA (Key-scheduling algorithm)
   for i in range(256):
      j = (j + S[i] + key[i % len(key)]) % 256
      S[i], S[j] = S[j], S[i]

   i = j = 0
   output = []
   # PRGA (Pseudo-random generation algorithm)
   for char in text:
      i = (i + 1) % 256
      j = (j + S[i]) % 256
      S[i], S[j] = S[j], S[i]
      output.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

   return ''.join(output)

ciphertext = RC4("Key", "Hello, World!")
plaintext = RC4("Key", ciphertext)  # Decrypt
print(plaintext)
print(ciphertext)
