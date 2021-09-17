#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the code implementing RSA.

@author: Josh Hicks
"""

from math import gcd
import random

def encrypt(mess, _e, _n):
    m2 = []
    for b in mess:
        _b = ord(b)
        m2.append(pow(_b, _e, _n))
    return m2

def decrypt(mess, _d, _n):
    m2 = []    
    for m in mess:
        _m = chr(pow(m, _d, _n))
        #print(_m,m)
        m2.append(_m)
    return ''.join(m2)

def relativePrime(num):
    rels = []
    for i in range(2,num):
        if gcd(num, i) == 1:
            rels.append(i)
    return rels[random.randint(0, len(rels) - 1)]

def inverse(_e, _phi):
    for i in range(2, _phi):
        if (_e * i) % _phi == 1:
            return i

def getPrimeNumbers(m = 1000, n = 1000):      
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]     
    p = 2
    while(p * p <= n):          
        # If prime[p] is not changed, then it is
        # a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    #print(len(prime))
    primes = []
    # Return all prime numbers
    for p in range(m, n):
        if prime[p]:
            primes.append(p)
    return primes

primeNumbers = getPrimeNumbers(150, 1000)    

def getRandomPrime():
    return primeNumbers[random.randint(0, len(primeNumbers))]

def getRSAKeys():
    # Random prime numbers
    p = getRandomPrime()
    q = getRandomPrime()
    # Public Key
    n = p * q
    phi = (p - 1) * (q - 1)
    e = relativePrime(phi)
    # Private Key
    d = inverse(e,phi)
    #print(d)
    #print(relativePrime(phi))
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
    integrationTest()