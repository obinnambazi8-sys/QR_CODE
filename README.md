QR Code Encoder & Decoder

Project Overview

This is a simple Python-based QR Code Encoder and Decoder that allows users to generate QR codes from text or URLs and decode existing QR code images to retrieve their stored information.

The project uses a menu-driven interface that allows users to choose between creating a new QR code or decoding an existing one.

It was built to practise Python programming, functions, loops, conditional statements, user input handling, and working with external Python libraries.

Features

QR Code Generation: Converts text or URLs into QR code images.

Custom File Naming: Allows users to choose a filename for their generated QR code.

QR Code Decoding: Reads existing QR code images and extracts their stored information.

Input Validation: Checks for empty inputs and ensures that decoding files use the .png extension.

Image Validation: Checks whether an image can be opened before attempting to decode it.

Main Menu: Provides a continuous menu-driven interface using a while loop.

Error Handling: Displays appropriate messages when an image cannot be opened or a QR code cannot be decoded.

Technologies & Libraries

Python 3 – Main programming language.

qrcode – Used to generate QR code images.

OpenCV (cv2) – Used to read and decode QR code images.
Key Python Concepts Practised

Through this project, I practised:

Importing and using external Python libraries.

Creating and calling functions.

Using while loops to build a main menu.

Implementing if, elif, and else conditional statements.

Handling and validating user input.

Working with image files.

Using OpenCV's QRCodeDetector() to detect and decode QR codes.

Saving generated files programmatically.


