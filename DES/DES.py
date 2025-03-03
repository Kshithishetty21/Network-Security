import random

def string_to_binary(s):
    return ''.join(format(ord(i), '08b') for i in s)

def binary_to_string(b):
    chars = [b[i:i+8] for i in range(0, len(b), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def generate_keys(binary_text):
    l = len(binary_text) // 2
    left, right = binary_text[:l], binary_text[l:]
    shifts = [2, 3, 6, 7, 1, 6, 5, 9]  # Key shift values
    keys = []

    for i in range(8):
        nl = bin(int(left, 2) << shifts[i])[2:].zfill(l)
        nr = bin(int(right, 2) << shifts[i])[2:].zfill(l)
        new_key = nr + nl
        random_indices = random.sample(range(len(new_key)), 8)
        new_key = ''.join(new_key[i] for i in range(len(new_key)) if i not in random_indices)
        keys.append(new_key)

    return keys

def encrypt(binary_text, keys):
    encrypted = binary_text
    for key in keys:
        encrypted = ''.join(str(int(encrypted[i]) ^ int(key[i % len(key)])) for i in range(len(encrypted)))
    return encrypted

def decrypt(encrypted_text, keys):
    decrypted = encrypted_text
    for key in reversed(keys):  # Reverse order for decryption
        decrypted = ''.join(str(int(decrypted[i]) ^ int(key[i % len(key)])) for i in range(len(decrypted)))
    return decrypted

# User input
plaintext = input("Enter a string: ")
binary_plaintext = string_to_binary(plaintext)
keys = generate_keys(binary_plaintext)

# Encrypt
ciphertext = encrypt(binary_plaintext, keys)
print("Encrypted Binary:", ciphertext)

# Decrypt
decrypted_binary = decrypt(ciphertext, keys)
decrypted_text = binary_to_string(decrypted_binary)
print("Decrypted Text:", decrypted_text)
