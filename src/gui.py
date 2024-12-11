# src/gui.py
import tkinter as tk
from tkinter import END
from .crypto_utils import sToN, nToS, encrypt, decrypt

class TwoUserGUI:
    def __init__(self, master, keys_a, keys_b):
        self.master = master
        self.master.title("Two-User Encryption Interface")

        # keys_a = (e1, d1, n1, E2, D2, N2)
        # keys_b = (e2, d2, n2, E1, D1, N1)
        self.e1, self.d1, self.n1, self.E2, self.D2, self.N2 = keys_a
        self.e2, self.d2, self.n2, self.E1, self.D1, self.N1 = keys_b

        frame_a = tk.Frame(master, padx=10, pady=10, bd=2, relief=tk.GROOVE)
        frame_b = tk.Frame(master, padx=10, pady=10, bd=2, relief=tk.GROOVE)
        frame_a.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        frame_b.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # User A Widgets
        tk.Label(frame_a, text="User A Input:").grid(row=0, column=0, pady=5)
        self.user_a_input = tk.Entry(frame_a, width=50)
        self.user_a_input.grid(row=0, column=1, pady=5)

        tk.Label(frame_a, text="User A Output:").grid(row=1, column=0, pady=5)
        self.user_a_output = tk.Entry(frame_a, width=50)
        self.user_a_output.grid(row=1, column=1, pady=5)
        tk.Button(frame_a, text="Copy A Output", command=self.copy_a_output).grid(row=1, column=2, padx=5)

        tk.Button(frame_a, text="Encrypt", command=self.user_a_encrypt).grid(row=2, column=0, pady=5)
        tk.Button(frame_a, text="Decrypt", command=self.user_a_decrypt).grid(row=2, column=1, pady=5)

        # User B Widgets
        tk.Label(frame_b, text="User B Input:").grid(row=0, column=0, pady=5)
        self.user_b_input = tk.Entry(frame_b, width=50)
        self.user_b_input.grid(row=0, column=1, pady=5)

        tk.Label(frame_b, text="User B Output:").grid(row=1, column=0, pady=5)
        self.user_b_output = tk.Entry(frame_b, width=50)
        self.user_b_output.grid(row=1, column=1, pady=5)
        tk.Button(frame_b, text="Copy B Output", command=self.copy_b_output).grid(row=1, column=2, padx=5)

        tk.Button(frame_b, text="Encrypt", command=self.user_b_encrypt).grid(row=2, column=0, pady=5)
        tk.Button(frame_b, text="Decrypt", command=self.user_b_decrypt).grid(row=2, column=1, pady=5)

    def copy_a_output(self):
        output_text = self.user_a_output.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(output_text)
        self.master.update()

    def copy_b_output(self):
        output_text = self.user_b_output.get()
        self.master.clipboard_clear()
        self.master.clipboard_append(output_text)
        self.master.update()

    def user_a_encrypt(self):
        # A → B: Encrypt with (d1, E2, n1, N2)
        plaintext = self.user_a_input.get()
        if not plaintext:
            return
        msg_num = sToN(plaintext)
        encrypted_num = encrypt(msg_num, self.d1, self.E2, self.n1, self.N2)
        self.user_a_output.delete(0, END)
        self.user_a_output.insert(0, str(encrypted_num))

    def user_a_decrypt(self):
        # B → A: Decrypt with (D1, e2, n2, N1)
        try:
            enc_num = int(self.user_a_input.get())
        except ValueError:
            return
        decrypted_num = decrypt(enc_num, self.D1, self.e2, self.n2, self.N1)
        plaintext = nToS(decrypted_num)
        self.user_a_output.delete(0, END)
        self.user_a_output.insert(0, plaintext)

    def user_b_encrypt(self):
        # B → A: Encrypt with (d2, E1, n2, N1)
        plaintext = self.user_b_input.get()
        if not plaintext:
            return
        msg_num = sToN(plaintext)
        encrypted_num = encrypt(msg_num, self.d2, self.E1, self.n2, self.N1)
        self.user_b_output.delete(0, END)
        self.user_b_output.insert(0, str(encrypted_num))

    def user_b_decrypt(self):
        # A → B: Decrypt with (D2, e1, n1, N2)
        try:
            enc_num = int(self.user_b_input.get())
        except ValueError:
            return
        decrypted_num = decrypt(enc_num, self.D2, self.e1, self.n1, self.N2)
        plaintext = nToS(decrypted_num)
        self.user_b_output.delete(0, END)
        self.user_b_output.insert(0, plaintext)
