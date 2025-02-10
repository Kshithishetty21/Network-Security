# Hill Cipher
The Hill Cipher is a polygraphic substitution cipher based on linear algebra. It encrypts messages by transforming blocks of letters into vectors and then multiplying these vectors by an invertible matrix (the key) modulo 26. Each letter is represented by a number (A=0, B=1, ..., Z=25). The resulting vector is then converted back into letters to form the ciphertext.

## Working of Hill Cipher

### Encryption Process

1. **Key Matrix**: 
   - An *n*×*n* invertible matrix is used as the key. The determinant of this matrix must be non-zero and not divisible by 2 or 13 (the prime factors of 26, the number of letters in the alphabet).

2. **Text Representation**: 
   - Each letter is converted to a number (A=0, B=1, ..., Z=25). The plaintext is divided into blocks of *n* letters.

3. **Matrix Multiplication**: 
   - Each block of letters (represented as a vector) is multiplied by the key matrix. The result is taken modulo 26 to produce the ciphertext.

### Decryption Process

1. **Inverse Key Matrix**: 
   - To decrypt the ciphertext, the inverse of the key matrix is computed.

2. **Matrix Multiplication**: 
   - The ciphertext vector is multiplied by the inverse key matrix, allowing the original plaintext to be recovered.

## Steps to Run the Program

1. **Install Required Libraries**: 
   - Ensure you have Python and NumPy installed on your system.

2. **Input Plaintext**: 
   - Run the program and input the plaintext you wish to encrypt.

3. **Input Key Matrix**: 
   - Specify the size of the key matrix (e.g., 2 for a 2x2 matrix) and enter the key matrix values row by row.

4. **Encryption**: 
   - The program will output the ciphertext.

5. **Decryption**: 
   - The program will also decrypt the ciphertext back to the original plaintext and display it.

## Output:
Here are sample outputs for the Hill-Cipher code:

## References

- **GeeksforGeeks**: [Hill Cipher](https://www.geeksforgeeks.org/hill-cipher-cryptography/)
- **Wikipedia**: [Hill Cipher](https://en.wikipedia.org/wiki/Hill_cipher)
- **Crypto Corner**: [Hill Cipher](https://cryptocorner.com/hill-cipher)

