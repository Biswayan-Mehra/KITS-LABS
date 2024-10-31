s0 = [["01", "00", "11", "10"],
      ["11", "10", "01", "00"],
      ["00", "10", "01", "11"],
      ["11", "01", "11", "10"]]

s1 = [["00", "01", "10", "11"],
      ["10", "00", "01", "11"],
      ["11", "00", "01", "00"],
      ["10", "01", "00", "11"]]

def xor(s1, s2):
    return "".join("1" if s1[i] != s2[i] else "0" for i in range(len(s1)))

def get_sub_keys(key):
    p10 = "".join(key[i-1] for i in [3, 5, 2, 7, 4, 10, 1, 9, 8, 6])
    left, right = p10[:5], p10[5:]
    left, right = left[1:] + left[0], right[1:] + right[0]
    key_1 = left + right
    key_1 = key_1[5] + key_1[2] + key_1[6] + key_1[3] + key_1[7] + key_1[4] + key_1[9] + key_1[8]
    key_2 = left[2:] + left[:2] + right[2:] + right[:2]
    key_2 = key_2[5] + key_2[2] + key_2[6] + key_2[3] + key_2[7] + key_2[4] + key_2[9] + key_2[8]
    return key_1, key_2

def IP(b):
    return "".join(b[i-1] for i in [2, 6, 3, 1, 4, 8, 5, 7])

def IP_inv(b):
    return "".join(b[i-1] for i in [4, 1, 3, 5, 7, 2, 8, 6])

def E_P(r):
    return "".join(r[i-1] for i in [4, 1, 2, 3, 2, 3, 4, 1])

def sbox_sub(b4, s):
    row, col = int(b4[0] + b4[3], 2), int(b4[1] + b4[2], 2)
    return s[row][col]

def F(nibble, subkey):
    xor_op = xor(E_P(nibble), subkey)
    xor_l, xor_r = xor_op[:4], xor_op[4:]
    l1, r1 = sbox_sub(xor_l, s0), sbox_sub(xor_r, s1)
    combined = l1 + r1
    p4 = "".join(combined[i-1] for i in [2, 4, 3, 1])
    return p4

def fk(b, subkey):
    l, r = b[:4], b[4:]
    return xor(l, F(r, subkey)) + r

def SW(b):
    return b[4:] + b[:4]

def chunk(stream, l):
    i = 0
    chunks = []
    while i < len(stream):
        chunks.append(stream[i:i+l])
        i += l
    return chunks

def sdes_encrypt(text, key):
    key_1, key_2 = get_sub_keys(key)
    chunks = chunk(text, 8)
    chunks = [IP(b) for b in chunks]
    cipher = []
    for b in chunks:
        cipher.append(IP_inv(fk(SW(fk(b, key_1)), key_2)))
    return " ".join(cipher)

def sdes_decrypt(cipher, key):
    key_1, key_2 = get_sub_keys(key)
    chunks = chunk(cipher, 8)
    chunks = [IP(b) for b in chunks]
    text = []
    for b in chunks:
        text.append(IP_inv(fk(SW(fk(b, key_2)), key_1)))
    return " ".join(text)

# Testing the S-DES implementation
print("URK21CS1004")
key = "1100011110"  # 10-bit key
text = "00100011 10011010"
print("Text:", text)

cipher = sdes_encrypt(text.replace(" ", ""), key)
print("Cipher:", cipher)

print("Decrypted:", sdes_decrypt(cipher.replace(' ', ''), key))
