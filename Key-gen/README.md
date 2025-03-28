#  **Secure Key Management System**

###  **Introduction**
The **Secure Key Management System** is a Python-based implementation that provides:
- **RSA Key Generation**: Generates RSA key pairs for encryption and decryption.
- **Diffie-Hellman Key Exchange**: Establishes a shared secret key securely.
- **AES Encryption and Decryption**: Uses AES encryption with a shared key for secure message exchange.
- **Digital Signatures**: Ensures message integrity and authenticity.
- **Key Expiration and Revocation**: Revokes expired or compromised keys.
- **Persistent Storage**: Stores keys in files for future use.

---

###  **Tech Stack**
- Python
- `pycryptodome` and `cryptography` libraries for encryption, key exchange, and digital signature management.
- JSON for storing revoked keys.

---

###  **How It Works**

####  **1. RSA Key Generation**
- The system generates **RSA key pairs** for two users (User A and User B).
- The keys are stored in `.pem` files:
  - `userA_private.pem`
  - `userA_public.pem`
  - `userB_private.pem`
  - `userB_public.pem`
- RSA keys are used for **signing messages** and verifying their authenticity.

---

####  **2. Diffie-Hellman Key Exchange**
- The system generates **Diffie-Hellman parameters** for secure key exchange.
- Each user generates their **DH private and public keys**.
- The shared AES key is derived from the exchanged public keys using **HKDF**.

---

####  **3. AES Encryption and Decryption**
- The **AES-GCM** mode is used for **message encryption and decryption**.
- The message (`"Hello this is INS task"`) is encrypted using the shared AES key and transmitted.
- The receiver **decrypts** the message using the same shared AES key, ensuring confidentiality.

---

####  **4. Digital Signature**
- The sender (User A) signs the message with their **RSA private key**.
- The receiver (User B) verifies the signature using the **RSA public key**.
- This ensures the message's authenticity and integrity.

---

####  **5. Key Expiration and Revocation**
- The system sets an **expiration date** (30 days by default) for RSA keys.
- If the key is expired, it is added to the **revoked keys list** (`revoked_keys.json`).
- The system checks whether a key is revoked before using it.

---

###  **Usage Instructions**

1. **Install Dependencies**
```bash
pip install pycryptodome cryptography

