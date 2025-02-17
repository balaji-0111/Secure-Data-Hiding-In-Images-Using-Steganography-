import cv2
import os
import random
import hashlib

# Caesar Cipher Encryption
def encrypt_message(message, shift):
    encrypted_msg = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_msg += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_msg += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_msg += char
    return encrypted_msg

# Caesar Cipher Decryption
def decrypt_message(message, shift):
    return encrypt_message(message, -shift)

# Hash the password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Read the image
img_path = "my-pic.jpg"  # Replace with the correct image path
if not os.path.exists(img_path):
    print("Image file not found!")
    exit()

img = cv2.imread(img_path)
if img is None:
    print("Failed to load image!")
    exit()

# Input secret message and password
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Encrypt the message
shift = 3  # Shift value for Caesar Cipher
encrypted_msg = encrypt_message(msg, shift)

# Hash the password
hashed_password = hash_password(password)

# Create dictionaries for character mapping
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Randomly select pixels to hide the message
random.seed(int(hashed_password, 16))  # Use hashed password as seed for randomness
pixel_indices = random.sample(range(img.shape[0] * img.shape[1]), len(encrypted_msg))

# Hide the message in the image
for i, char in enumerate(encrypted_msg):
    row = pixel_indices[i] // img.shape[1]
    col = pixel_indices[i] % img.shape[1]
    img[row, col, 0] = d[char]  # Store in the blue channel

# Save the encrypted image
encrypted_img_path = "encrypted-Img.jpg"
cv2.imwrite(encrypted_img_path, img)
print(f"Encrypted image saved as {encrypted_img_path}")

# Open the encrypted image (Windows)
os.system(f"start {encrypted_img_path}")

# Decryption
pas = input("Enter passcode for Decryption: ")
if hash_password(pas) == hashed_password:
    decrypted_msg = ""
    for i in range(len(encrypted_msg)):
        row = pixel_indices[i] // img.shape[1]
        col = pixel_indices[i] % img.shape[1]
        decrypted_msg += c[img[row, col, 0]]
    decrypted_msg = decrypt_message(decrypted_msg, shift)
    print("Decrypted message:", decrypted_msg)
else:
    print("YOU ARE NOT AUTHORIZED")
