import math
from math import gcd
import random

message = "qwertyuiopasdfghjklzxcvbnm"

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
            rels.append( i)
    return rels[random.randint(0,len(rels) - 1)]

def inverse(_e, _phi):
    for i in range(2,phi):
        if (_e * i) % _phi == 1:
            return i

        
    
def getPrimeNumbers(m = 1000 ,n = 1000):      
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
    # Print all prime numbers
    for p in range(m, n):
        if prime[p]:
            primes.append(p)
    return primes

primeNumbers = getPrimeNumbers(150, 1000)    

def getRandomPrime():
    return primeNumbers[random.randint(0, len(primeNumbers))]

#print(primeNumbers)    
#Random prime numbers
p = getRandomPrime()
q = getRandomPrime()

#Public Key
n = p * q
phi = (p - 1 ) * ( q - 1)
e = relativePrime(phi)

#Private Key
d = inverse(e,phi)
#print(d)

#print(relativePrime(phi))    
encrypted = encrypt(message, e, n)
#print(encrypted)

decrypted = decrypt(encrypted, d, n)
print(decrypted)
