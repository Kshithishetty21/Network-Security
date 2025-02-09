
def encryp():
    """Encrypt the plaintext using the monoalphabetic cipher."""
    plain=msg.upper()
    encr=""
    for i in plain:
        if(i.isalpha()):
            ind=p.index(i)
            encr+=CipherKey[ind]
        else:
            encr+=i
    return encr

def decryp():
    """Decrypt the ciphertext using the monoalphabetic cipher."""
    decryp=""
    for i in encrypted:
        if(i.isalpha()):
            ind=CipherKey.index(i)
            decryp+=p[ind]
        else:
            decryp+=i
    return decryp

p="ABCDEFGHIJKLMNOPKRSTUVWXYZ"
CipherKey="QWERTYUIOPASDFGHJKLZXCVBNM"
print("Key:" ,CipherKey)
msg=input("Enter the Plaintext: ")
encrypted=encryp()
print("Encrypted message : " ,encrypted)
decrypted=decryp()
print("Decrypted message : ",decrypted)
