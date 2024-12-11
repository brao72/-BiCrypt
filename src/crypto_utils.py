# src/crypto_utils.py
import math

# Character mapping
char_map = {' ': 40}
for i in range(26):
    char_map[chr(ord('a') + i)] = 11 + i
inv_char_map = {v: k for k, v in char_map.items()}

def sToN(s):
    n = 0
    for ch in s:
        n = n * 100 + char_map[ch]
    return n

def nToS(n):
    s = ""
    while n > 0:
        val = n % 100
        if val not in inv_char_map:
            # If this happens, it means we didn't decrypt properly
            return "ERROR"
        s = inv_char_map[val] + s
        n //= 100
    return s

def encrypt(m, d_sender, E_receiver, n_sender, N_receiver):
    # sign-then-encrypt
    signed = pow(m, d_sender, n_sender)  # sign with sender's private
    encrypted = pow(signed, E_receiver, N_receiver)  # encrypt with receiver's public
    return encrypted

def decrypt(c, D_receiver, e_sender, n_sender, N_receiver):
    # decrypt-then-verify
    decrypted_signed = pow(c, D_receiver, N_receiver)  # decrypt with receiver's private
    m = pow(decrypted_signed, e_sender, n_sender)       # verify with sender's public
    return m
