# RSA Encryption Algorithm

## Introduction

RSA (Rivest-Shamir-Adleman) is a widely used public-key cryptographic system that enables secure data transmission. It is based on the mathematical properties of prime numbers and modular arithmetic. RSA is used for secure data transmission, digital signatures, and key exchange. The security of RSA relies on the difficulty of factoring the product of two large prime numbers.

## Working of RSA

The RSA algorithm consists of the following steps:

### Step 1: Key Generation
1. **Choose two distinct prime numbers** `p` and `q`.
2. **Calculate `n`**: Multiply `p` and `q` to get `n` (i.e., `n = p * q`).
3. **Calculate Euler's Totient** `phi`: Compute `phi(n) = (p - 1) * (q - 1)`.
4. **Choose an integer `e`**: Select an integer `e` such that `1 < e < phi(n)` and `gcd(e, phi(n)) = 1`. This `e` will be the public exponent.
5. **Calculate `d`**: Find `d` such that `(d * e) % phi(n) = 1`. This `d` will be the private exponent.

### Step 2: Encryption
1. **Convert the message** `m` into an integer (if necessary).
2. **Encrypt the message**: Compute the ciphertext `c` using the formula `c = (m^e) % n`.

### Step 3: Decryption
1. **Decrypt the ciphertext**: Retrieve the original message using the formula `m = (c^d) % n`.

### Example Usage
To use the RSA algorithm, run the provided Python code. You will be prompted to enter the values for `p`, `q`, and the message `m`. The program will then output the encrypted message and the decrypted message.

### Sample Output
- ![image](https://github.com/user-attachments/assets/4e0bd576-0e98-431a-824f-aa8cabe3f2a1)

### Note
- Ensure that the prime numbers `p` and `q` are large enough to provide adequate security.
- The algorithm's security is based on the difficulty of factoring the product of two large primes.

