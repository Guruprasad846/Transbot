import cv2
import pytesseract
from PIL import Image
from gtts import gTTS
from playsound import playsound
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract'
img=cv2.imread(r"C:\Users\Guruprasad\Pictures\Screenshots\Screenshot (464).png")
img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# shape of image

img_h,img_w, img_c =img.shape
boxes=pytesseract.image_to_boxes(Image.open(r"C:\Users\Guruprasad\Pictures\Screenshots\Screenshot (464).png"))
# for box in boxes.splitlines():
#     box=box.split(" ")
    
#     x, y, w, h = [int(x) for x in box[1: 5]]
#    # print (x, y, w, h)
#     cv2.rectangle(img,(x, img_h - y), (w, img_h -h),(0, 0, 255), 1)
#     cv2.putText(img, box[0],(x,img_h -y + 20 ), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255),1)
# cv2.imshow("Image",img)

boxes= pytesseract.image_to_data(Image.open(r"C:\Users\Guruprasad\Pictures\Screenshots\Screenshot (464).png"))   
sentence = ""
for i, box in enumerate(boxes.splitlines()):
    # print(box)
    if i==0:
        continue
    box = box.split()
    #print(box)
    if len(box) == 12:
        x, y, w, h = [int(x) for x in box[6: 10]]
        print(x, y, w, h)
        cv2.rectangle(img,(x, y), (x+w, y+h),(0, 0, 255), 1)
        cv2.putText(img, box[11], (x, y + 30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,255),1)
        sentence += box[11] +" "


print(sentence)
sound =gTTS(text = sentence , lang='en')
sound.save("sound.mp3")
playsound("sound.mp3")
cv2.imshow("Image",img)
if cv2.waitKey(0) & 0xFF==ord('q'):
    cv2.destroyAllWindows()
 


   