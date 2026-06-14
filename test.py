import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

img = cv2.imread("uploads/image_0.jpg")

print("Image loaded:", img is not None)

if img is not None:
    text = pytesseract.image_to_string(img)

    print("OCR OUTPUT:")
    print(repr(text))