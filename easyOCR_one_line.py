###############################
#
#Simple OCR - Object Character Recognition script
#for one sentence in a picture
#
###############################

#importing the needed libraries
import easyocr
import cv2
import matplotlib.pyplot as plt

#makes an easyocr reader object with danish language and we ask then to run on the CPU rather than the GPU
reader = easyocr.Reader(lang_list=['da'], gpu=False)

#The path to where the image is stored
IMAGE_PATH = '/Users/simons/OCR/images/2.png'

#A variable called output which gonna store the returned data from the reader
output = reader.readtext(IMAGE_PATH, paragraph=True) #detail=0 for only text

#pointing out one sentence from the list that we only are interested in
read_output = output[1]


#reading the original image
img = cv2.imread(IMAGE_PATH)
#Setting the font that is used on the image
font = cv2.FONT_HERSHEY_SIMPLEX
#making a spacer, which helps us to place the translated text on the image
spacer = 500
#making the green box that surrounds the translated text
top_left = read_output[0][0]
bottom_right = read_output[0][2]
#getting the text in the returned list
text = read_output[1]
#making the rectangle
img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
#putting the text for the picture
img = cv2.putText(img,text,(2,spacer), font, 0.5,(0,255,0),2,cv2.LINE_AA)
#making a spacer
spacer+=30
#plotting it
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()

#printing the detected text for further use to the terminal
question_asked = read_output[1]
print(question_asked)
