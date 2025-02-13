from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# AES Encryption Function
def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv + ciphertext  # Prepend IV for decryption

# AES Decryption Function
def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size).decode()

# Columnar Transposition Encryption Function
def columnar_transposition_encrypt(plaintext, key):
    key_length = len(key)
    columns = [''] * key_length

    # Fill the columns
    for i, char in enumerate(plaintext):
        columns[i % key_length] += char

    # Sort columns based on the key
    sorted_columns = sorted(range(len(key)), key=lambda k: key[k])
    ciphertext = ''.join(columns[i] for i in sorted_columns)
    return ciphertext

# Columnar Transposition Decryption Function
def columnar_transposition_decrypt(ciphertext, key):
    key_length = len(key)
    num_rows = len(ciphertext) // key_length
    columns = [''] * key_length

    # Fill the columns based on the key order
    sorted_indices = sorted(range(len(key)), key=lambda k: key[k])
    for i in range(key_length):
        col_index = sorted_indices[i]
        columns[col_index] = ciphertext[i * num_rows:(i + 1) * num_rows]

    # Read the plaintext row-wise
    plaintext = ''
    for i in range(num_rows):
        for col in columns:
            if i < len(col):
                plaintext += col[i]
    return plaintext

# Hybrid Encryption Function
def hybrid_encrypt(plaintext, aes_key, transposition_key):
    aes_ciphertext = aes_encrypt(plaintext, aes_key)
    transposition_ciphertext = columnar_transposition_encrypt(aes_ciphertext.hex(), transposition_key)
    return transposition_ciphertext

# Hybrid Decryption Function
def hybrid_decrypt(ciphertext, aes_key, transposition_key):
    transposition_plaintext = columnar_transposition_decrypt(ciphertext, transposition_key)
    aes_plaintext = aes_decrypt(bytes.fromhex(transposition_plaintext), aes_key)
    return aes_plaintext

# Example Usage
if __name__ == "__main__":
    # Generate a random 128-bit key (16 bytes)
    aes_key = os.urandom(16)  # For demonstration, you can also use a fixed key

    # User input for plaintext and transposition key
    plaintext = input("Enter the plaintext message to encrypt: ")
    transposition_key = input("Enter the transposition key: ")

    print("\n--- Encryption Process ---")
    encrypted = hybrid_encrypt(plaintext, aes_key, transposition_key)
    print("Encrypted (Hex):", encrypted)

    print("\n--- Decryption Process ---")
    decrypted = hybrid_decrypt(encrypted, aes_key, transposition_key)
    print("Decrypted:", decrypted)