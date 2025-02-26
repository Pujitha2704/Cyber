# Steganography
Image Steganography – Hide Data Inside Images

📌 Project Overview

This project implements image steganography, a technique for securely hiding secret messages within digital images. By modifying pixel values, the project ensures data remains concealed while maintaining the original image's appearance. It provides a simple yet effective way to prevent hackers from intercepting sensitive information.

🚀 Features

✅ Securely hides text messages within an image

✅ Password protection for message decryption

✅ Minimal distortion in the stego-image

✅ Supports multiple image formats (JPG, PNG, BMP)

✅ Lightweight and easy-to-use

🛠 Technologies Used

Programming Language: Python

Libraries: OpenCV (cv2), NumPy, OS

Security Mechanism: Password Authentication

🛠 How It Works

Encryption:

The user enters a secret message and passcode.
The message is converted into ASCII values and embedded into the image pixels.
A modified image is generated with hidden data.

Decryption:

The user provides the encrypted image and correct passcode.
The program extracts hidden text from the image.
If the passcode is incorrect, access is denied.

📌 Future Scope

🔹 Integration with AES/RSA encryption for enhanced security

🔹 AI-based steganography to improve data hiding efficiency

🔹 Support for audio/video steganography

🔹 Cloud-based secure data sharing system

📜 License

This project is open-source and available under the MIT License.


This project is licensed under the MIT License.
