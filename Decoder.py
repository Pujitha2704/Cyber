def decode_image(encrypted_image_path, original_message_length, correct_password):
    img = cv2.imread(encrypted_image_path)

    if img is None:
        print("Error: Could not load encrypted image.")
        return
    
    c = {i: chr(i) for i in range(255)}  # ASCII to character mapping

    n, m, z = 0, 0, 0
    decrypted_message = ""

    entered_password = input("Enter passcode for decryption: ")
    
    if entered_password == correct_password:
        for _ in range(original_message_length):
            decrypted_message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3  # Cycle through RGB channels
        
        print("Decryption successful! Message:", decrypted_message)
    else:
        print("YOU ARE NOT AUTHORIZED!")

# Example usage:
decode_image("encryptedImage.jpg", len(message), passcode)
