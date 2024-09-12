import math

# Function to factorize n to find p and q
def factorize_n(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

# Function to calculate modular inverse (for d)
def modinv(e, phi):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Function to decrypt each value using RSA formula m = c^d % n
def rsa_decrypt(c_list, d, n):
    message = ""
    for c in c_list:
        m = pow(c, d, n)
        message += chr(m)  # Convert decrypted number to corresponding ASCII character
    return message

# Given values
n = 1079
e = 43
ciphertext = "996 894 379 631 894 82 379 852 631 677 677 194 893"
c_values = list(map(int, ciphertext.split()))

# Step 1: Factorize n to get p and q
p, q = factorize_n(n)
if not p or not q:
    raise Exception("Failed to factorize n")

# Step 2: Calculate phi(n)
phi = (p - 1) * (q - 1)

# Step 3: Calculate private key d
d = modinv(e, phi)

# Step 4: Decrypt the message
decrypted_message = rsa_decrypt(c_values, d, n)

# Output the results
print(f"p = {p}, q = {q}")
print(f"Private key d = {d}")
print(f"Decrypted message: {decrypted_message}")
