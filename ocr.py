import pytesseract
from PIL import Image



def convert_box_ocr(image):
    img = Image.fromarray(image)
    config_ = ('-l eng --oem 3 --psm 8')
    text = pytesseract.image_to_string(img,config=config_)
    return text