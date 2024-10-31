def encrypt_columnar_transposition(text, key):
   col_count = len(key)
   rows = [text[i:i + col_count] for i in range(0, len(text), col_count)]
   key_order = sorted(range(len(key)), key=lambda x: key[x])
   return ''.join(''.join(row[i] for row in rows if i < len(row)) for i in key_order)

def decrypt_columnar_transposition(cipher, key):
   col_count = len(key)
   n = len(cipher)
   rows_count = (n + col_count - 1) // col_count
   key_order = sorted(range(col_count), key=lambda x: key[x])
   rail_len = [n // col_count + (i < n % col_count) for i in range(col_count)]

   rail, idx = [''] * col_count, 0
   for i in key_order:
      rail[i] = cipher[idx:idx + rail_len[i]]
      idx += rail_len[i]

   return ''.join(''.join(rail[i][r] for i in range(col_count) if r < len(rail[i])) for r in range(rows_count))

print("URK21CS1004")
print("Enter Text: ", end= "")
text = input()

print("Enter Key: ", end= "")
key = input()
cipher = encrypt_columnar_transposition(text.replace(" ", ""), key)
print("Encrypted:", cipher)

decrypted_text = decrypt_columnar_transposition(cipher, key)
print("Decrypted:", decrypted_text)
