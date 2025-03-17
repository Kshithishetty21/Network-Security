# Diffie-Hellman Key Exchange Algorithm

## Introduction
The **Diffie-Hellman Key Exchange** is a cryptographic protocol that allows two parties to securely share a secret key over a public channel. It is widely used in secure communication protocols such as SSL/TLS.

This Python script demonstrates the Diffie-Hellman Key Exchange algorithm by computing public and shared keys for two users.

## Working of Diffie-Hellman Algorithm
1. Choose a **prime number (q)** and a **primitive root (a)**.
2. Each party selects a **private key (Xa for A and Xb for B)**.
3. Compute the **public keys**:
   - `Ya = (a^Xa) mod q` (Public key of A)
   - `Yb = (a^Xb) mod q` (Public key of B)
4. Compute the **shared secret key**:
   - `Ka = (Yb^Xa) mod q` (Shared key for A)
   - `Kb = (Ya^Xb) mod q` (Shared key for B)
5. Both parties obtain the same shared secret key **Ka == Kb**.

## Sample Output:
Run the script and enter the required values:
- ![Screenshot (34)](https://github.com/user-attachments/assets/58ebe9d0-5b61-45d0-b2fd-7adb01bcd156)


## Reference Links
- [Diffie-Hellman Key Exchange (Wikipedia)](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- [Cryptography Basics - Diffie-Hellman](https://www.tutorialspoint.com/cryptography/cryptography_diffie_hellman.htm)

