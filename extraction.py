import pytesseract
import cv2

# import image
image = cv2.imread('1.1.jpg')

# convertion to gray scale reduces complexity & noise, thus OCR works better
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('temp/index_gray.png', gray)
text = pytesseract.image_to_string(gray)
print(text)

# blur the image
blur = cv2.GaussianBlur(gray, (7,7), 0)

cv2.imwrite('temp/index_blur.png', blur)
text = pytesseract.image_to_string(blur)
print(text)

# Use Threshold = color inversion = identifying cols
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

cv2.imwrite('temp/index_thresh.png', thresh)
text = pytesseract.image_to_string(thresh)
print(text)

# kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 30))

cv2.imwrite('temp/index_kernel.png', kernel)


# dilate
dilate = cv2.dilate(thresh, kernel, iterations=1)

cv2.imwrite('temp/index_dilate.png', dilate)
text = pytesseract.image_to_string(dilate)
print(text)

# contours
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if len(cnts) == 2 else cnts[1]

cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

for c in cnts:
    x, y, w,h = cv2.boundingRect(c)
    cv2.rectangle(image, (x, y), (x+w, y+h), (36, 255, 12), 2) 

cv2.imwrite('temp/index_bbox.png', image)
# text = pytesseract.image_to_string(cnts)
# print(text)