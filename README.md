# Two-User Encryption

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Table of Contents

- [About The Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About The Project

**Two-User Encryption** is a demonstration application that facilitates secure communication between two users using RSA-like cryptography. The application provides a user-friendly interface built with Tkinter, allowing users to encrypt and decrypt messages seamlessly. This project is intended for educational purposes, illustrating the fundamentals of public-key cryptography and GUI development in Python.

## Features

- **RSA Key Generation:** Automatically generates RSA key pairs for two users, ensuring secure encryption and decryption.
- **Encryption & Decryption:** Users can encrypt messages to send securely and decrypt received messages with ease.
- **User-Friendly GUI:** Intuitive interface built with Tkinter, featuring input/output fields and actionable buttons.
- **Copy Functionality:** Easily copy encrypted messages to share between users without manual selection.
- **Error Handling:** Robust error messages guide users through correct usage and inform them of any issues.
- **Unit Testing:** Comprehensive tests ensure the reliability of cryptographic functions and conversions.

## Tech Stack

### Frontend

- **Python 3.x:** The primary programming language used for developing the application.
- **Tkinter:** Python's standard GUI library used to create the graphical user interface.

### Backend

- **RSA Cryptography:** Implements RSA-like encryption and decryption mechanisms for secure communication.
- **Custom Utilities:** Includes functions for converting strings to numerical representations and vice versa.
- **Unit Testing:** Utilizes Python's `unittest` framework to validate the functionality of cryptographic components.

## Installation

Follow these comprehensive steps to set up the **Two-User Encryption** project on your local machine.

### Prerequisites

- **Python 3.x** installed on your system. You can download it from [here](https://www.python.org/downloads/).
- **Git** installed on your system. You can download it from [here](https://git-scm.com/downloads).

### Steps

1. **Clone the Repository**

   Open your terminal and run:

   ```bash
   git clone https://github.com/brao72/two_user_encryption.git

2. **Navigate to the Project Directory**


   ```bash
   cd two_user_encryption

3. **Verify Installation**

   Ensure that all required files and directories are present. Your project structure should resemble the following:

   ```bash
   two_user_encryption/
   ├── src/
   │   ├── __init__.py
   │   ├── keygen.py
   │   ├── crypto_utils.py
   │   ├── gui.py
   │   └── main.py
   ├── tests/
   │   ├── __init__.py
   │   └── test_crypto.py
   ├── .gitignore
   ├── README.md
   └── requirements.txt

4. **Run the applcaion**

   Launch the Two-User Encryption application using the following command:

   ```bash
   python3 -m src.main

  ## Usage

Launch the **Two-User Encryption** application to start encrypting and decrypting messages.

### How to Use the GUI

1. **User A Panel (Left Side):**
   - **Input:** Enter your plaintext message in the "User A Input" field.
   - **Encrypt:** Click the "Encrypt" button to encrypt the message. The encrypted message will appear in the "User A Output" field.
   - **Copy:** Click the "Copy A Output" button to copy the encrypted message to your clipboard.
   - **Decrypt:** To decrypt a message sent from User B, paste the encrypted message into the "User A Input" field and click "Decrypt". The original message will appear in the "User A Output" field.

2. **User B Panel (Right Side):**
   - **Input:** Enter your plaintext message in the "User B Input" field.
   - **Encrypt:** Click the "Encrypt" button to encrypt the message. The encrypted message will appear in the "User B Output" field.
   - **Copy:** Click the "Copy B Output" button to copy the encrypted message to your clipboard.
   - **Decrypt:** To decrypt a message sent from User A, paste the encrypted message into the "User B Input" field and click "Decrypt". The original message will appear in the "User B Output" field.

### Example Workflow

1. **User A Sends a Message to User B:**
   - User A types "hello world" in the "User A Input" field.
   - Clicks "Encrypt". The encrypted message appears in "User A Output".
   - Clicks "Copy A Output" to copy the encrypted message.
   - User B pastes the encrypted message into "User B Input" and clicks "Decrypt".
   - The original message "hello world" appears in "User B Output".

2. **User B Sends a Message to User A:**
   - User B types "goodbye" in the "User B Input" field.
   - Clicks "Encrypt". The encrypted message appears in "User B Output".
   - Clicks "Copy B Output" to copy the encrypted message.
   - User A pastes the encrypted message into "User A Input" and clicks "Decrypt".
   - The original message "goodbye" appears in "User A Output".

## Future Enhancements

While the current version of **Two-User Encryption** provides fundamental encryption and decryption functionalities, several enhancements can be implemented to improve its features and security:

- **Enhanced Character Support:**
  - Expand the character mapping to include uppercase letters, numbers, and special characters.
  
- **Larger Key Sizes:**
  - Implement larger prime numbers (e.g., 2048-bit keys) for enhanced security.
  
- **User Authentication:**
  - Add authentication mechanisms to verify user identities before allowing encryption/decryption operations.
  
- **Message Signing and Verification:**
  - Incorporate digital signatures to ensure message integrity and authenticity.
  
- **Persistent Key Storage:**
  - Allow users to save and load their RSA key pairs securely.
  
- **GUI Improvements:**
  - Enhance the interface with better layouts, themes, and user experience features.
  
- **Logging and Audit Trails:**
  - Implement logging to track encryption and decryption activities for audit purposes.
  
- **Error Handling Enhancements:**
  - Provide more detailed error messages and handle a wider range of exceptions gracefully.
  
- **Integration with Messaging Platforms:**
  - Enable direct communication through popular messaging platforms with encryption support.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html) – Python's standard GUI library.
- [RSA Algorithm](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) – Public-key cryptosystem used for secure data transmission.
- [Python GitHub Templates](https://github.com/github/gitignore) – For creating effective `.gitignore` files.
   





