import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract'
print(pytesseract.image_to_string(Image.open(r"C:\Users\Guruprasad\Pictures\Screenshots\Screenshot (466).png")))
print(pytesseract.image_to_boxes(Image.open(r"C:\Users\Guruprasad\Pictures\Screenshots\Screenshot (466).png")))
boxes=pytesseract.image_to_boxes(Image.open(r"C:\Users\Guruprasad\Pictures\Screenshots\Screenshot (466).png"))
for box in boxes.splitlines():
    box=box.split(" ")
    
    x, y, w, h = [int(x) for x in box[1: 5]]
    print (x, y, w, h)