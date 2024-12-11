# src/keygen.py
import math, random

def is_prime(num):
    # Implement Miller-Rabin or a deterministic test for small ranges
    if num < 2:
        return False
    # Check small primes
    for p in [2,3,5,7,11,13,17,19,23]:
        if num == p:
            return True
        if num % p == 0:
            return False
    
    # Miller-Rabin
    return miller_rabin(num)

def miller_rabin(n, k=5):
    # Implement Miller-Rabin Test
    if n < 2:
        return False
    # Check even
    if n % 2 == 0:
        return n == 2

    # Write n-1 as 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x != 1 and x != n - 1:
            for __ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
    return True

def generate_prime(k):
    if k == 1:
        return 2
    while True:
        num = random.randint(10**(k-1), 10**k - 1)
        if is_prime(num):
            return num

def generate_rsa_keys(p_bits=10, P_bits=100):
    # Generate small primes for (p, q) and large for (P, Q)
    p = generate_prime(p_bits)
    q = generate_prime(p_bits)
    n = p*q

    P = generate_prime(P_bits)
    Q = generate_prime(P_bits)
    N = P*Q

    phi = (p-1)*(q-1)
    Phi = (P-1)*(Q-1)

    e = generate_e(phi, Phi)
    d = pow(e, -1, phi*Phi) # if we consider combined modulus or adapt
    # Alternatively, generate separate keys for "signature" and "encryption"
    # depending on your chosen scheme.

    # For simplicity, assume we just return all components
    return p,q,P,Q,n,N,e,d

def generate_e(phi, Phi):
    # Just pick an e that is coprime with phi and Phi
    # Example:
    while True:
        e = random.randint(2, phi*Phi - 1)
        if math.gcd(e, phi*Phi) == 1:
            return e
