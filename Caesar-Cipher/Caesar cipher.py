import string
p = input("Enter a Plaintext: ") 
k = int(input("Enter the key: "))
chars = list(string.ascii_letters)

def encrypt(str):
    encstr = ""
    for char in str:
        if char in chars: 
            j = chars.index(char)  
            j = (j + k) % 26  
            encstr += chars[j]  
    return encstr


def decrypt(str):
    decstr = ""
    for char in str:
        if char in chars:  
            j = chars.index(char)  
            j = (j - k) % 26  
            decstr += chars[j]  
    return decstr

encrypted = encrypt(p)  
print("Encrypted message:", encrypted)
decrypted = decrypt(encrypted)  
print("Decrypted message:", decrypted)
