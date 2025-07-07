import pytesseract
import cv2

# import image
img = cv2.imread('1.jpg')

# convertion to gray scale reduces complexity & noise, thus OCR works better
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('temp/index_gray.png', gray)

text = pytesseract.image_to_string(gray)
print(text)

# blur the image
blur = cv2.GaussianBlur(gray, (7,7), 0)

cv2.imwrite('temp/index_blur.png', blur)

text1 = pytesseract.image_to_string(blur)
print(text1)
