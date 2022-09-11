from pdf2image import convert_from_path
pages = convert_from_path('mypdf.pdf', 500)
pages[x].save('full_page_image.jpg', 'JPEG') #where x is your page number minus one


import cv2
import numpy as np
full_page_image = cv2.imread('full_page_image.jpg')
image_to_be_added = cv2.imread('image_to_be_added.jpg')
final_image = full_page_image.copy()
final_image[100:400,100:400,:] = image_to_be_added[100:400,100:400,:] #adjust the numbers according to the dimensions of the image_to_be_added
cv2.imwrite(final_image.jpg, final_image)

from PIL import Image
final_image2 = Image.open(r'final_image.jpg')
final_image3 = final_image2.convert('RGB')
final_image3.save(r'final_pdf.pdf')
