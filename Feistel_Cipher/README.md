# Feistel Cipher Implementation

## Introduction

The Feistel cipher is a symmetric structure used in the construction of block ciphers. It divides the input data into two halves and processes them through multiple rounds of permutation and substitution. The Feistel structure allows for the encryption and decryption processes to be very similar, making it efficient and secure.

## Working

1. **Input Data**: The plaintext is divided into two halves.
2. **Key Mixing**: A key is used to modify one half of the data.
3. **Round Function**: A round function is applied to one half, and the result is combined with the other half using XOR.
4. **Swapping**: The two halves are swapped.
5. **Multiple Rounds**: The process is repeated for a specified number of rounds.
6. **Final Output**: The two halves are combined to produce the ciphertext.

## Steps to Run the Program

- **Input the String**: When prompted, enter a string that you want to encrypt.
- **Input the Key**: When prompted, enter a key that will be used for encryption.
- **Run the Program**: Execute the code. The program will output the decrypted plaintext.

## Output
Here’s an example of how the program runs:
- ![Screenshot (29)](https://github.com/user-attachments/assets/d2878fee-5adb-4647-b3b7-f18c886b1f12)

## References

- [Wikipedia - Feistel Cipher](https://en.wikipedia.org/wiki/Feistel_cipher)
