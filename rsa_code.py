#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the code implementing RSA.

@author: Josh Hicks
"""

from math import gcd
import random

# Constants for getRandomPrime()
MIN_PRIME_GEN = 1 << 16 + 1
MAX_PRIME_GEN = 1 << 64 - 1
FERMAT_TESTS = 32

def encrypt(mess, _e, _n):
    return [pow(ord(m), _e, _n) for m in mess]

def decrypt(mess, _d, _n):
    return "".join([chr(pow(m, _d, _n)) for m in mess])

def relativePrime(num):
    while True:
        rel = random.randint(1, num - 1)
        if gcd(rel, num) == 1:
            return rel

def extendedGcd(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, d) = extendedGcd(b, a % b)
    return (y, x - a // b * y, d)

def inverse(_e, _phi):
    return extendedGcd(_e, _phi)[0] % _phi

def getRandomPrime(m = MIN_PRIME_GEN, n = MAX_PRIME_GEN):
    # Generate a random prime in [m..n].
    has_prime = False
    while not has_prime:
        num = random.randint(m, n)
        has_prime = True
        # Perform Fermat primality tests
        for i in range(FERMAT_TESTS):
            base = random.randint(1, num - 1)
            if not pow(base, num - 1, num) == 1:
                has_prime = False
                break
    return num

def getRSAKeys(unitTest = False):
    # Random prime numbers
    p, q = 0, 0
    if unitTest:
        p = getRandomPrime(17, 63)
        print("p =", p)
        q = getRandomPrime(17, 63)
        print("q =", q)
    else:
        p = getRandomPrime()
        q = getRandomPrime()
    # Public Key
    n = p * q
    if unitTest: print("n =", n)
    phi = (p - 1) * (q - 1)
    if unitTest: print("phi =", phi)
    e = relativePrime(phi)
    if unitTest: print("e =", e)
    # Private Key
    d = inverse(e, phi)
    if unitTest: print("d =", d)
    return (n, e, d)

"""
Integration test for RSA code above.

@author: Archer Murray
"""
def integrationTest():
    # Generate RSA keys
    print("Generating RSA keys, please wait...")
    (n, e, d) = getRSAKeys()
    print("RSA keys generated.")
    enc_messages = []
    choice = 0
    # Display user interface
    while not choice == 3:
        print("Who are you?")
        print("1. A public user")
        print("2. The owner of the keys")
        print("3. Exit program")
        choice = int(input("Enter your choice: "))
        # 1. A public user
        while choice == 1:
            print("As a public user, what would you like to do?")
            print("1. Send an encrypted message")
            print("2. Authenticate a digital signature")
            print("3. Log out")
            choice = int(input("Enter your choice: "))
            # 1. Send a message
            if choice == 1:
                msg = input("Enter a message: ")
                enc_messages.append(encrypt(msg, e, n))
                print("Message encrypted and sent.")
            # 2. Authenticate a signature
            elif choice == 2:
                print("Function not yet supported.")
            # Return to loop if not logged out
            if not choice == 3:
                choice = 1
            else:
                choice = 0
        # 2. The owner of the keys
        while choice == 2:
            print("As the owner of the keys, what would you like to do?")
            print("1. Decrypt a received message")
            print("2. Digitally sign a message")
            print("3. Log out")
            choice = int(input("Enter your choice: "))
            # 1. Decrypt a message
            if choice == 1:
                if len(enc_messages) == 0:
                    print("You have no messages available.")
                else:
                    print("The following messages are available:")
                    for i in range(len(enc_messages)):
                        print(i + 1, ". (length = ",
                              len(enc_messages[i]), ")", sep = '')
                    choice = int(input("Enter your choice: "))
                    if choice < 1 or choice > len(enc_messages):
                        print("Out of range, try again.")
                    else:
                        msg = decrypt(enc_messages[choice - 1], d, n)
                        print("Decrypted message:", msg)
                    choice = 0
            # 2. Sign a message
            elif choice == 2:
                print("Function not yet supported.")
            # Return to loop if not logged out
            if not choice == 3:
                choice = 2
            else:
                choice = 0

# Run integration test
if __name__ == '__main__':
    print("--- Unit test ---")
    (n, e, d) = getRSAKeys(True)
    message = "Hello"
    mess_arr = [ord(c) for c in message]
    print("Original message:", message, "=", mess_arr)
    enc_arr = encrypt(message, e, n)
    print("Encrypted message:", enc_arr)
    message = decrypt(enc_arr, d, n)
    mess_arr = [ord(c) for c in message]
    print("Decrypted message:", message, "=", mess_arr)
    print("--- Integeration test ---")
    integrationTest()