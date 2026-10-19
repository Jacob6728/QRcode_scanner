# OpenCV QR Code Scanner

A simple, beginner-friendly QR Code Scanner built using **Python and OpenCV**.

This project uses your computer's webcam to detect and decode QR codes in real time. When a QR code is detected, the scanner draws a green box around it and prints its contents in the terminal.

## Features

- Real-time QR code detection using a webcam
- Automatically decodes QR code contents
- Draws a green outline around detected QR codes
- Displays scanned information in the terminal
- Prevents repeated printing of the same QR code
- Press **Q** to exit the scanner
- Beginner-friendly Python code with comments

## Technologies Used

- **Python 3** — Main programming language
- **OpenCV** — Computer vision library for detecting and decoding QR codes

## Installation

### Step 1: Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/opencv-qr-scanner.git
```

Navigate into the project folder:

```bash
cd opencv-qr-scanner
```

### Step 2: Install Dependencies

Make sure Python 3 and pip are installed.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## How to Run

Start the QR Code Scanner by running:

```bash
python qr_scanner.py
```

Your webcam should open automatically.

1. Hold a QR code in front of the camera.
2. Wait for the scanner to detect it.
3. A green box will appear around the QR code.
4. The decoded information will appear in the terminal.
5. Press **Q** to close the scanner.

## Example Output

```text
QR Code Scanner Started!
Hold a QR code in front of the camera.
Press 'q' to quit the scanner.

QR Code Detected!
Content: https://www.google.com
```

## How It Works

The scanner uses OpenCV's built-in `QRCodeDetector` class.

1. `cv2.VideoCapture(0)` opens the webcam.
2. `camera.read()` captures video frames.
3. `detectAndDecode()` searches for QR codes and reads their contents.
4. `cv2.line()` draws a green outline around detected QR codes.
5. `cv2.imshow()` displays the live video.
6. `cv2.waitKey()` checks whether the user pressed Q.

## Project Structure

```text
opencv-qr-scanner/
├── qr_scanner.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE
```

## Future Improvements

- Add a graphical user interface (GUI)
- Support multiple QR codes simultaneously
- Save scanned QR codes to a CSV file
- Add sound notifications for successful scans
- Allow QR code scanning from image files

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Contributions

Contributions, suggestions, and improvements are welcome! Feel free to fork the repository and submit a pull request.