# Vigenère Cipher

## Introduction

The Vigenère cipher is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution. It employs a keyword, where each letter of the keyword refers to a shift in the alphabet. The cipher is named after Blaise de Vigenère, a 16th-century French diplomat.

## Working

1. **Keyword Selection**: Choose a keyword that will be used for encryption and decryption. The keyword should be repeated or truncated to match the length of the plaintext.

2. **Encryption Process**:
   - For each letter in the plaintext, find the corresponding letter in the keyword.
   - Calculate the shift based on the position of the keyword letter in the alphabet (A=0, B=1, ..., Z=25).
   - Shift the plaintext letter by the calculated amount, wrapping around the alphabet if necessary.

3. **Decryption Process**:
   - The decryption process is similar but involves shifting in the opposite direction using the same keyword.

## Steps to Run the Program
- **Input the Plaintext and Key**: When prompted, enter the plaintext (the message you want to encrypt) and the key (the keyword used for encryption).

- **Run the Program**: Execute the code. The program will output the encrypted text and then decrypt it back to the original plaintext.

## Output

Here’s an example of how the program runs:
- ![image](https://github.com/user-attachments/assets/e8f6c5aa-9abc-4883-b5ef-556d5bc415da)




## References

- [Wikipedia - Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
- [Cryptography and Network Security](https://www.amazon.com/Cryptography-Network-Security-Principles-Practice/dp/0134444280) (Book reference for deeper understanding)

