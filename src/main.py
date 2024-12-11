# src/main.py
from .gui import TwoUserGUI
from .keygen import generate_rsa_keys
import tkinter as tk

def main():
    # Generate keys for both users
    # Adjust as needed for correct key usage.
    # For demonstration, let's assume generate_rsa_keys returns sets of keys you can split up.
    # In practice, adjust according to your chosen protocol.

    # user_a_keys: (e1, d1, n1, E2, D2, N2)
    # user_b_keys: (e2, d2, n2, E1, D1, N1)
    # This might require manual assignment after calling generate_rsa_keys multiple times.
    
    # Just as an example (not cryptographically accurate):
    p1,q1,P1,Q1,n1,N1,e1,d1 = generate_rsa_keys(10, 100)
    p2,q2,P2,Q2,n2,N2,e2,d2 = generate_rsa_keys(10, 100)

    # For demonstration, assume same structure as in previous code snippet:
    # In a real scenario, generate separate sets of keys and decide which ones to use as public/private.
    # Here we will just reuse the generated keys in a similar way.

    E1 = e1  # Just reusing generated values; in a real scenario, these might differ
    D1 = d1
    E2 = e2
    D2 = d2

    # Keys for A and B (based on the example GUI)
    user_a_keys = (e1, d1, n1, E2, D2, N2)
    user_b_keys = (e2, d2, n2, E1, D1, N1)

    root = tk.Tk()
    app = TwoUserGUI(root, user_a_keys, user_b_keys)
    root.mainloop()

if __name__ == "__main__":
    main()
