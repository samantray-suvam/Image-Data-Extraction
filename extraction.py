from PIL import Image
from matplotlib import pyplot as plt
import pytesseract

image_file = "pdf_pages/img-01.jpg"
img=Image.open(image_file)

# Matplotlib display function
def display(img_pil):
    dpi = 80

    height, width = img_pil.size
    figsize = width / float(dpi), height / float(dpi)

    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    ax.imshow(img_pil, cmap='gray')
    plt.show()

display(img)

# OCR with pytesseract
try:
    print("🔍 Extracting text using pytesseract...")
    extracted_text = pytesseract.image_to_string(image_file)
    print("\n📄 Extracted Text:")
    print(extracted_text)
    
    # Optional: save to file
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)
    print("✅ Text saved to extracted_text.txt")
except Exception as e:
    print(f"❌ OCR failed: {e}")
