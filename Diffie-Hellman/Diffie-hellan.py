def diffie_hellman(a, q, Xa, Xb):
    # Compute public keys
    Ya = pow(a, Xa, q)  # Public key of A
    Yb = pow(a, Xb, q)  # Public key of B

    print("Public key of A:", Ya)
    print("Public key of B:", Yb)

    # Compute shared keys
    Ka = pow(Yb, Xa, q)  # Shared key for A
    Kb = pow(Ya, Xb, q)  # Shared key for B

    print("Shared key for A:", Ka)
    print("Shared key for B:", Kb)

    # Verify that both shared keys are the same
    assert Ka == Kb, "Shared keys do not match!"

# Example usage
a = int(input("Enter a prime number: "))
q = int(input("Enter a primitive root: "))
Xa = int(input("Enter the private key of A: "))
Xb = int(input("Enter the private key of B: "))

diffie_hellman(a,q, Xa, Xb)