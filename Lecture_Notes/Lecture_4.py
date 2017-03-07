import random

def encrypt(msg):
    n_msg =[]
#prints every char in a string
    for s in msg:
        n_msg.append(random.randint(0,1))


def decrypt(msg):
    pass

encrypted_message = encrypt("Hello")
