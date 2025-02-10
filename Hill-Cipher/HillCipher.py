import numpy as np


substitution = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
               'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}


inverse_substitution = {value: key for key, value in substitution.items()}

def encrypt(plain_text, key_matrix):
    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % len(key_matrix) != 0:
padding_length = len(key_matrix) - (len(plain_text) % len(key_matrix))
        plain_text += 'X' * padding_length

    cipher_text = ''
    for i in range(0, len(plain_text), len(key_matrix)):
        block = plain_text[i:i+len(key_matrix)]
        block_vector = np.array([substitution[ch] for ch in block])
encrypted_vector = np.dot(key_matrix, block_vector) % 26
        encrypted_block = ''.join([inverse_substitution[num] for num in encrypted_vector])
        cipher_text += encrypted_block

    return cipher_text

def decrypt(cipher_text, key_matrix):
    cipher_text = cipher_text.upper().replace(" ", "")

    
    determinant = int(round(np.linalg.det(key_matrix)))
determinant_mod_inverse = pow(determinant, -1, 26)
    adjugate_matrix = np.round(np.linalg.inv(key_matrix) * determinant).astype(int) % 26
    inverse_key_matrix = (determinant_mod_inverse * adjugate_matrix) % 26

    plain_text = ''
    for i in range(0, len(cipher_text), len(key_matrix)):
        block = cipher_text[i:i+len(key_matrix)]
        block_vector = np.array([substitution[ch] for ch in block])
decrypted_vector = np.dot(inverse_key_matrix, block_vector) % 26
        decrypted_block = ''.join([inverse_substitution[num] for num in decrypted_vector])
        plain_text += decrypted_block

    return plain_text.strip('X')


plain_text = input("Enter the plain text: ")
key_matrix_size = int(input("Enter the size of the key matrix (e.g., 2 for 2x2): "))
print(f"Enter the {key_matrix_size}x{key_matrix_size} key matrix row by row:")
key_matrix = []
for _ in range(key_matrix_size):
    row = list(map(int, input().split()))
    key_matrix.append(row)
key_matrix = np.array(key_matrix)


cipher_text = encrypt(plain_text, key_matrix)
print("Cipher Text:", cipher_text)


decrypted_text = decrypt(cipher_text, key_matrix)
print("Decrypted Text:", decrypted_text)
