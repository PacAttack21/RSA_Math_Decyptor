This script was primarily created for the purpose of CTF challenges.

The program takes in 3 inputs.

n: This is the modulus for both the public and private keys. It is the product of two prime numbers 
p and q. In RSA, the value of n is part of the public key and is used in both encryption and decryption.

e: This is the public exponent, part of the public key. It is used in the encryption process. It is chosen such that it has no common factors with 𝜙(𝑛), where ϕ(n) is the Euler’s totient function of n.

c: This represents the ciphertext, which is the encrypted message. It’s a list of integers that have been produced using the public key during encryption. These integers need to be decrypted to reveal the original message.

This would be an example of the inputs we need:
![image](https://github.com/user-attachments/assets/1481b7c0-64fe-49d8-8181-e34c910f038d)

To change the values, change the follwing lines in the program
```
# Given values
n = 1079
e = 43
ciphertext = "996 894 379 631 894 82 379 852 631 677 677 194 893"
c_values = list(map(int, ciphertext.split()))
```

After Changing the values run the program (python3 rsa_decrypt.py) and it will give you:

p and q: which are the prim variables used to calculate n

d: This is the private exponent (part of the private key)

The decrypted message

Output:
![RSA](https://github.com/user-attachments/assets/c0fa7792-8d45-4cf2-ab0c-7c51a9a8abe9)
