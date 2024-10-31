def key_scheduling(key):
    s = [i for i in range(256)]
    j = 0
    for i in range(256):
        j = (j + s[i] + ord(key[i % len(key)])) % 256
        s[i], s[j] = s[j], s[i]
    return s

def rc4_encrypt(text, key):
    i, j = 0, 0
    s = key_scheduling(key)
    cipher = ""
    for letter in text:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % 256
        K = s[t]
        cipher += chr(K ^ ord(letter))
    return cipher

def rc4_decrypt(cipher, key):
    i, j = 0, 0
    s = key_scheduling(key)
    text = ""
    for letter in cipher:
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        t = (s[i] + s[j]) % 256
        K = s[t]
        text += chr(K ^ ord(letter))
    return text

# Test the RC4 encryption and decryption
print("URK21CS1004")
plaintext = "HELLO Hee ByE"
print("Original text:", plaintext)

cipher = rc4_encrypt(plaintext, "key")
print("Cipher:", cipher)

decrypted_text = rc4_decrypt(cipher, "key")
print("Decrypted:", decrypted_text)
