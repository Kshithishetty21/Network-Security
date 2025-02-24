def encrypt_v(p, k):
    k = k.upper()
    ciphertext = ""
    k_index = 0
    for char in p.upper():
        if char.isalpha():
            shift = ord(k[k_index]) - ord('A')
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            k_index = (k_index + 1) % len(k)
        else:
            ciphertext += char
    return ciphertext

def decrypt_v(p, k):
    k = k.upper()
    ciphertext = ""
    k_index = 0
    for char in p.upper():
        if char.isalpha():
            shift = ord(k[k_index]) - ord('A')
            ciphertext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            k_index = (k_index + 1) % len(k)
        else:
            ciphertext += char
    return ciphertext

p = input("Enter the plaintext:")
k = input("Enter the key:")
n=encrypt_v(p, k)
print("Encrypted:",n)
print("Decrypted:", decrypt_v(n, k))
