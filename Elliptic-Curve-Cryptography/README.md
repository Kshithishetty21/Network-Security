# Elliptic Curve Cryptography (ECC) Key Exchange

## Introduction
Elliptic Curve Cryptography (ECC) is a modern asymmetric cryptographic algorithm used for secure communication. ECC provides the same level of security as traditional algorithms like RSA but with smaller key sizes, making it more efficient.

This Python script demonstrates ECC key exchange using the **tinyec** library, implementing encryption key generation via elliptic curve point multiplication.

## How the ECC Algorithm Works
1. **Select an Elliptic Curve**:  
   The script uses the `brainpoolP256r1` curve from the `tinyec` registry.

2. **Generate Private and Public Keys**:  
   - Each party (Sender and Receiver) generates a **random private key**.
   - Compute the **public key** using:  
     `Public Key = Private Key * Generator Point (G)`

3. **Generate Encryption Key**:  
   - A **random cipher private key** is generated.
   - Compute the **cipher public key** as:  
     `Cipher Public Key = Cipher Private Key * Generator Point`
   - Compute the **shared encryption key** as:  
     `Encryption Key = Cipher Public Key * Cipher Private Key`

4. **Share Public Keys**:  
   Both parties compute the same shared encryption key independently.

   
## Sample Output
### Installation
First, install the required package:
```sh
pip install tinyec
```
-![Screenshot (35)](https://github.com/user-attachments/assets/5f9859fb-da6b-4951-b895-e8148d9fa441)




