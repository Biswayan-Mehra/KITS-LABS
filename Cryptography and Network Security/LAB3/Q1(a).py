def encrypt_rail_fence_zigzag(text, key):
   rail = [''] * key
   row, step = 0, 1
   for char in text:
      rail[row] += char
      row += step
      if row == 0 or row == key - 1:
         step *= -1
   return ''.join(rail)

def decrypt_rail_fence_zigzag(cipher, key):
   n = len(cipher)
   rail_len = [0] * key
   row, step = 0, 1
   for _ in range(n):
      rail_len[row] += 1
      row += step
      if row == 0 or row == key - 1:
         step *= -1

   rail, idx = [''] * key, 0
   for i in range(key):
      rail[i] = cipher[idx:idx + rail_len[i]]
      idx += rail_len[i]

   result, row, step = [], 0, 1
   for _ in range(n):
      result.append(rail[row][0])
      rail[row] = rail[row][1:]
      row += step
      if row == 0 or row == key - 1:
         step *= -1
   return ''.join(result)

text = "GeeksforGeeks"
key = 3
cipher = encrypt_rail_fence_zigzag(text.replace(" ", ""), key)
print("Encrypted (Zigzag):", cipher)

decrypted_text = decrypt_rail_fence_zigzag(cipher, key)
print("Decrypted (Zigzag):", decrypted_text)
