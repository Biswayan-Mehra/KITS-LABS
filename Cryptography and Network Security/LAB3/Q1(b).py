def encrypt_rail_fence_diagonal(text, key):
   rail = [''] * key
   for i, char in enumerate(text):
      rail[i % key] += char
   return ''.join(rail)

def decrypt_rail_fence_diagonal(cipher, key):
   n = len(cipher)
   rail_len = [n // key + (1 if i < n % key else 0) for i in range(key)]
   rail = []
   index = 0
   for length in rail_len:
      rail.append(cipher[index:index + length])
      index += length
   return ''.join(rail[i % key][i // key] for i in range(n))

text = "GeeksforGeeks"
key = 3
cipher = encrypt_rail_fence_diagonal(text.replace(" ", ""), key)
print("Encrypted (Diagonal):", cipher)

decrypted_text = decrypt_rail_fence_diagonal(cipher, key)
print("Decrypted (Diagonal):", decrypted_text)
