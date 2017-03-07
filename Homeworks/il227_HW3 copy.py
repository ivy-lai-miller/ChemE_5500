import numpy as np
import random

def encrypt(message, N, E):
    encrypted = []
    for M in message:
        cipher = (ord(M)**E)%N
        encrypted.append(cipher)
    return encrypted

#print encrypt("Hello world", 17947,7)

def decrypt(encrypted_message, N, D):
    decrypted = ''
    for cipher_d in encrypted_message:
        M_decrypt = (cipher_d**D)%N
        decrypted += chr(M_decrypt)

    return decrypted

a = encrypt("msg",17947,7)
b = decrypt(a,17947,10103)

#test code
#print ("msg"==b)

#print decrypt(encrypt("Hello World!",17947,7),17947,10103)

#challenge
def generate_key():
    #returns (N,E,D)
    possible_primes = get_primes_in_range(130,200)
    P = random.choice(possible_primes)
    Q = P
    while Q==P:
        Q = random.choice(possible_primes)
    N = Q*P
    X = (P-1)*(Q-1)

    #Find E that is relatively prime to X
    X_prime_divisors = get_prime_divisors(X)
    prime_less_X = get_primes_in_range(2,X)
    possible_E= []
    for a in prime_less_X:
        if a not in X_prime_divisors:
            possible_E.append(a)
    E = random.choice(possible_E)

    #Find D st D*E = 1modX
    D=0
    for testD in range (1,X):
        if 1==(testD*E)%X:
            D = testD
    return "(N,E,D)=" + str((N,E,D))


def is_prime(p):
    if p < 2:
        return False
    #check if any divisors between 2 and p.
    #If p=2, then the range is empty and function will return True
    for x in range(2,int(p**0.5)):
        if p%x == 0:
            return False
    return True

def get_primes_in_range(low,high):
    result = []
    for y in range (low,high):
        if is_prime(y):
            result.append(y)

    return result

#print get_primes_in_range(1,1000)

def get_prime_divisors(N):
    primes = get_primes_in_range(2,N+1)
    result = []
    for p in primes:
        if N%p==0:
            result.append(p)
    return result

#print get_prime_divisors(100)

print generate_key()
