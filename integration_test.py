#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is the integration test interface for RSA.

@author: Archer Murray
"""

import rsa_code

print("Generating RSA keys, please wait...")
(n, e, d) = rsa_code.getRSAKeys()
print("RSA keys generated.")

enc_messages = []
choice = 0

while not choice == 3:
    print("Who are you?")
    print("1. A public user")
    print("2. The owner of the keys")
    print("3. Exit program")
    choice = int(input("Enter your choice: "))
    
    while choice == 1:  # A public user
        print("As a public user, what would you like to do?")
        print("1. Send an encrypted message")
        print("2. Authenticate a digital signature")
        print("3. Log out")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:  # Send a message
            msg = input("Enter a message: ")
            enc_messages.append(rsa_code.encrypt(msg, e, n))
            print("Message encrypted and sent.")
        
        elif choice == 2:  # Authenticate a signature
            print("Function not yet supported.")
        
        if not choice == 3:  # Return to loop if not logged out
            choice = 1
        else:
            choice = 0
    
    while choice == 2:  # The owner of the keys
        print("As the owner of the keys, what would you like to do?")
        print("1. Decrypt a received message")
        print("2. Digitally sign a message")
        print("3. Log out")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:  # Decrypt a message
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
                    msg = rsa_code.decrypt(
                        enc_messages[choice - 1], d, n)
                    print("Decrypted message:", msg)
                choice = 0
        
        elif choice == 2:  # Sign a message
            print("Function not yet supported.")
        
        if not choice == 3:  # Return to loop if not logged out
            choice = 2
        else:
            choice = 0