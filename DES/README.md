# **Data Encryption Standard (DES)**

## **Introduction**
The **Data Encryption Standard (DES)** is a symmetric-key block cipher that encrypts data in 64-bit blocks using a **56-bit key** over **16 rounds of processing**. It was widely used for securing sensitive data before being replaced by more advanced encryption algorithms like AES.

## **How DES Works**
1. **Initial Permutation (IP):** Rearranges the bits of the plaintext in a predefined order.
2. **Divide into Two Halves (L and R):** The 64-bit block is split into two 32-bit halves.
3. **16 Rounds of Encryption:**
   - Expand **R** from 32 to **48 bits** using an expansion permutation.
   - XOR with the **round key**.
   - Substitute using **S-Boxes**.
   - Apply a **P-Box permutation**.
   - XOR the result with **L**.
   - Swap **L and R**.
4. **Final Permutation (FP):** Reorders the bits to produce ciphertext.

## **Sample Output**
- ![Screenshot (32)](https://github.com/user-attachments/assets/c80bbda9-be71-4102-9f4d-7b6268b469a3)

