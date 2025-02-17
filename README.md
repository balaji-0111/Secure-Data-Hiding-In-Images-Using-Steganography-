# 🖼️SECURE DATA HIDING IN IMAGES USING STEGANOGRAPHY🔐

Welcome to the **Secure data hiding in images using steganography**! This project demonstrates how to hide secret messages within an image using steganography techniques. The message is encrypted using a **Caesar Cipher** and embedded into randomly selected pixels of the image. Perfect for secure communication! 🚀

---

## 🌟 Features

- **🔒 Encryption**: Encrypts the secret message using a Caesar Cipher.
- **🎲 Random Pixel Selection**: Hides the message in randomly selected pixels for added security.
- **🔐 Password Protection**: Uses SHA-256 hashing to secure the passcode.
- **📤 Decryption**: Retrieves and decrypts the hidden message with the correct passcode.
- **🖼️ Image Manipulation**: Uses OpenCV to process and save the encrypted image.

---

## 🛠️ Requirements
To run this project, you'll need the following tools and libraries:

1. Python 3.8 or Higher 🐍
Make sure you have Python installed on your system. You can download it from the official website: python.org.

To check your Python version, run:

2. OpenCV Library 📦
This project uses OpenCV for image processing. Install it using pip:

```bash
pip install opencv-python-headless
```
3. Hashing Library (SHA-256) 🔐
The hashlib library is used for password hashing. It comes pre-installed with Python, so no additional installation is required.

4. Random Library 🎲
   The random library is used for selecting random pixels in the image. It is also included in Python's standard library.

5. Operating System 💻
   This project is compatible with:
   -- Windows 🪟
   -- MacOS 🍏
   -- Linux 🐧

6. Image File 🖼️
You need an image file (e.g., mypic.jpg) to hide the secret message. Place the image in the same directory as the script.

## 🚀 Getting Started

1. Clone the Repository
  Clone this repository to your local machine:
  git clone https://github.com/yourusername/image-steganography.git

2. Navigate to the Project Directory
```bash
cd image-steganography
```

3. Add Your Image
Place your image file (e.g., mypic.jpg) in the project directory.

4. Run the Script
Execute the script to start the steganography process:
```bash
python steganography.py
```

## 🖥️ Usage

## 🔐Encrypting a Message

1. Run the script:
```bash
python steganography.py
```

2. Enter your secret message when prompted.

3. Enter a passcode for encryption.

4. The encrypted image will be saved as encryptedImg.jpg.

## 🔓🔑Decrypting a Message

1. Run the script again:
```bash
python steganography.py
```

2. Enter the passcode used during encryption.

3. If the passcode is correct, the hidden message will be displayed.

## 🖥️ Example

Enter secret message: Hello, World!

Enter a passcode: mypassword

Encrypted image saved as encrypted-Img.jpg

Enter passcode for Decryption: mypassword

Decrypted message: Hello, World!

## 🛡️ Security Notes

Password Strength: Use a strong passcode to ensure security.

Image Quality: The encrypted image may have slight quality loss due to pixel manipulation.

Randomization: The message is hidden in random pixels, making it harder to detect.
