import pytesseract
import cv2

# import image
image = cv2.imread('img-01.1.jpg')
# base_img = image.copy()

# convertion to gray scale reduces complexity & noise, thus OCR works better
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('temp/index_gray.png', gray)


# blur the image
blur = cv2.GaussianBlur(gray, (7,7), 0)
cv2.imwrite('temp/index_blur.png', blur)


# Use Threshold = color inversion = identifying cols
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imwrite('temp/index_thresh.png', thresh)


# kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
cv2.imwrite('temp/index_kernel.png', kernel)


# dilate
dilate = cv2.dilate(thresh, kernel, iterations=1)
cv2.imwrite('temp/index_dilate.png', dilate)


# contours
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cnts = cnts[0] if len(cnts) == 2 else cnts[1]

cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])

results = []
for c in cnts:
    x, y, w,h = cv2.boundingRect(c)
    if h>200 and w>20:
         roi = image[y:y+h, x:x+h]
         cv2.rectangle(image, (x, y), (x+w, y+h), (36, 255, 12), 2) 
         ocr_result = pytesseract.image_to_string(roi)
         ocr_result = ocr_result.split("\n")
         for item in ocr_result:
              results.append(item)

cv2.imwrite('temp/index_bbox.png', image)

# print (results)

for item in results:
     item = item.strip().replace('\n', '')
     item = item.split(' ')[0]
     
     if len(item) > 0:
          if item[0].isupper():
               print(item)