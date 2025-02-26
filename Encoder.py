import cv2
import os

def encode_image(image_path, secret_message, password):
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not load image.")
        return
    
    d = {chr(i): i for i in range(255)}  # Character to ASCII mapping

    n, m, z = 0, 0, 0

    for char in secret_message:
        img[n, m, z] = d[char]  # Modify pixel value
        n += 1
        m += 1
        z = (z + 1) % 3  # Cycle through RGB channels

    encrypted_image_path = "encryptedImage.jpg"
    cv2.imwrite(encrypted_image_path, img)
    os.system(f"start {encrypted_image_path}")  # Opens the image in Windows

    print("Message encoded successfully!")
    return encrypted_image_path, password  # Return encoded image path and password

# Example usage:
image_path = "mypic.jpg"  # Replace with actual image path
message = input("Enter secret message: ")
passcode = input("Enter a passcode: ")
encode_image(image_path, message, passcode)
