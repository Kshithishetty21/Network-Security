def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a
 
def rsa(p,q,m):
    n = p*q
    phi = (p-1)*(q-1)
    
    for i in range (2, phi):
        if(gcd(i,phi)==1):
            e = i
            break
    j = 0
    
    while True:
        if(j*e%phi) == 1:
                d = j
                break
        j+=1
    
    c = (m**e)%n
    print("Encrypted message : ",c)
    d = (c**d)%n
    print("Decrypted message : ",d)
    
p = int(input("Enter the value of p :"))
q = int(input("Enter the value of q :"))
m = int(input("Enter a message :"))
    
rsa (p,q,m)
