# This is the final version of the Eye-writer with two keyboards.
# In the line 305-311 a function is called to that segment where an arrow head is placed. If you click(blink) on that segment,
# a "y" variable changes its value. For all the letter it is given in the code that if the y=0, it takes the letters from the first picture, if it's 1, it takes the letters from the second picture.
# keyboard.png and keyboard2.png pictures have to be placed in the same folder where this program is runned.

import cv2 as cv         # opencv
import np                # library for array
import pyautogui         # library for mouse control, here we do not use it.
from gtts import gTTS    # Import the required module for text to speech conversion
import os                # # This module is imported so that we can play the converted audio

cap = cv.VideoCapture(1)   # for the PS3 eye type one in the bracket. If you want to use the inner camera of the computer, type 0.
print("Video starting")
cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv.CAP_PROP_FPS, 25)
print("Video started")
claver=cv.imread("keyboard.PNG")
claver2=cv.imread("keyboard2.PNG")
f = open("guru99.txt", "w")        # Opens the text file where we will write.
#gray_claver = cv.cvtColor(claver, cv.COLOR_RGB2GRAY)  # If you would like to have the mask on the displayed image, run this line too, and change the frame+clever to mask+gray_claver in the 170th line.
def waitcontours():
    while(1) :
        ret, frame = cap.read()

        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)  # name of the variable

        lower = np.array([160])
        upper = np.array([255])

        # smooth the image thresholded
        mask = cv.blur(cv.inRange(gray, lower, upper), ksize=(3, 3))

        contours, hierarchy = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
        if contours:
            break

y=0
x=1
while True:
    waitcontours()
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)   #name of the variable

    lower = np.array([220])
    upper = np.array([255])

    # smooth the image thresholded
    mask = cv.blur(cv.inRange(gray, lower, upper), ksize=(3, 3))

    contours, hierarchy = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    if contours :
        M = cv.moments(contours[0])
        M["m00"] != 0
        cX = int(M["m10"] / M["m00"])  # https://docs.opencv.org/trunk/d8/d23/classcv_1_1Moments.html
        cY = int(M["m01"] / M["m00"])
        #pyautogui.moveTo(cX, cY)  # If you want to move the mouse, run this line too.
        #print(cX, cY)             # If you want cX and cY to be printed out, run this line too.
        x=0
    else:                 # Here all the letters are programed for a specific segment. So when you blink at a point, that point will be taken as the letter, where the pupil was visible at last.
        if x == 0 :
            if cX > 0 and cX < 95 and cY >0 and cY < 120:
                if y == 0:
                    print("Q")          # These lines are to input the desired letters in a txt. file. This function slows down the process.
                    f.write("Q")
                    x=1
                elif y == 1:
                    print("(")  # These lines are to input the desired letters in a txt. file. This function slows down the process.
                    f.write("(")
                    x = 1
            elif cX > 95 and cX < 185 and cY >0 and cY < 120:
                if y == 0:
                    print("W")
                    f.write("W")
                    x = 1
                elif y == 1:
                    print("1")
                    f.write("1")
                    x = 1
            elif cX > 185 and cX < 275 and cY >0 and cY < 120:
                if y == 0:
                    print("E")
                    f.write("E")
                    x = 1
                elif y == 1:
                    print("2")
                    f.write("2")
                    x = 1
            elif cX > 275 and cX < 365 and cY >0 and cY < 120:
                if y == 0:
                    print("R")
                    f.write("R")
                    x = 1
                elif y == 1:
                    print("3")
                    f.write("3")
                    x = 1
            elif cX > 365 and cX < 455 and cY >0 and cY < 120:
                if y == 0:
                    print("T")
                    f.write("T")
                    x = 1
                elif y == 1:
                    print("4")
                    f.write("4")
                    x = 1
            elif cX > 455 and cX < 545 and cY >0 and cY < 120:
                if y == 0:
                    print("Y")
                    f.write("Y")
                    x = 1
                elif y == 1:
                    print("5")
                    f.write("5")
                    x = 1
            elif cX > 545 and cX < 640 and cY >0 and cY < 120:
                if y == 0:
                    print("U")
                    f.write("U")
                    x = 1
                elif y == 1:
                    print(")")
                    f.write(")")
                    x = 1
            elif cX > 0 and cX < 95 and cY > 120 and cY < 240:
                if y == 0:
                    print("A")
                    f.write("A")
                    x = 1
                elif y == 1:
                    print("[")
                    f.write("[")
                    x = 1
            elif cX > 95 and cX < 185 and cY > 120 and cY < 240:
                if y == 0:
                    print("S")
                    f.write("S")
                    x = 1
                elif y == 1:
                    print("6")
                    f.write("6")
                    x = 1
            elif cX > 185 and cX < 275 and cY > 120 and cY < 240:
                if y == 0:
                    print("D")
                    f.write("D")
                    x = 1
                elif y == 1:
                    print("7")
                    f.write("7")
                    x = 1
            elif cX > 275 and cX < 365 and cY > 120 and cY < 240:
                if y == 0:
                    print("F")
                    f.write("F")
                    x = 1
                elif y == 1:
                    print("8")
                    f.write("8")
                    x = 1
            elif cX > 365 and cX < 455 and cY > 120 and cY < 240:
                if y == 0:
                    print("G")
                    f.write("G")
                    x = 1
                elif y == 1:
                    print("9")
                    f.write("9")
                    x = 1
            elif cX > 455 and cX < 545 and cY > 120 and cY < 240:
                if y == 0:
                    print("H")
                    f.write("H")
                    x = 1
                elif y == 1:
                    print("0")
                    f.write("0")
                    x = 1
            elif cX > 545 and cX < 640 and cY > 120 and cY < 240:
                if y == 0:
                    print("J")
                    f.write("J")
                    x = 1
                elif y == 1:
                    print("]")
                    f.write("]")
                    x = 1
            elif cX > 0 and cX < 95 and cY > 240 and cY < 360:
                if y == 0:
                    print("I")
                    f.write("I")
                    x = 1
                elif y == 1:
                    print("/")
                    f.write("/")
                    x = 1
            elif cX > 95 and cX < 185 and cY > 240 and cY < 360:
                if y == 0:
                    print("O")
                    f.write("O")
                    x = 1
                elif y == 1:
                    print("+")
                    f.write("+")
                    x = 1
            elif cX > 185 and cX < 275 and cY > 240 and cY < 360:
                if y == 0:
                    print("P")
                    f.write("P")
                    x = 1
                elif y == 1:
                    print("!")
                    f.write("!")
                    x = 1
            elif cX > 275 and cX < 365 and cY > 240 and cY < 360:
                if y == 0:
                    print("K")
                    f.write("K")
                    x = 1
                elif y == 1:
                    print("?")
                    f.write("?")
                    x = 1
            elif cX > 365 and cX < 455 and cY > 240 and cY < 360:
                if y == 0:
                    print("L")
                    f.write("L")
                    x = 1
                elif y == 1:
                    print(".")
                    f.write(".")
                    x = 1
            elif cX > 455 and cX < 545 and cY > 240 and cY < 360:
                if y == 0:
                    print("N")
                    f.write("N")
                    x = 1
                elif y == 1:
                    print("-")
                    f.write("-")
                    x = 1
            elif cX > 545 and cX < 640 and cY > 240 and cY < 360:
                if y == 0:
                    print("M")
                    f.write("M")
                    x = 1
                elif y == 1:
                    print("\\")
                    f.write("\\")
                    x = 1
            elif cX > 0 and cX < 95 and cY > 360 and cY < 480:
                if y == 0:
                    print("Z")
                    f.write("Z")
                    x = 1
                elif y == 1:
                    print(":")
                    f.write(":")
                    x = 1
            elif cX > 95 and cX < 185 and cY > 360 and cY < 480:
                if y == 0:
                    print("X")
                    f.write("X")
                    x = 1
                elif y == 1:
                    print("'")
                    f.write("'")
                    x = 1
            elif cX > 185 and cX < 275 and cY > 360 and cY < 480:
                if y == 0:
                    print("C")
                    f.write("C")
                    x = 1
                elif y == 1:
                    print(",")
                    f.write(",")
                    x = 1
            elif cX > 275 and cX < 365 and cY > 360 and cY < 480:
                if y == 0:
                    print("V")
                    f.write("V")
                    x = 1
                elif y == 1:
                    print("=")
                    f.write("=")
                    x = 1
            elif cX > 365 and cX < 455 and cY > 360 and cY < 480:
                if y == 0:
                    print("B")
                    f.write("B")
                    x = 1
                elif y == 1:
                    print("%")
                    f.write("%")
                    x = 1
            elif cX > 455 and cX < 545 and cY > 360 and cY < 480:
                if y == 0:
                    print(" ")
                    f.write(" ")
                    x = 1
                elif y == 1:
                    break
            elif cX > 545 and cX < 640 and cY > 360 and cY < 480:
                if y == 0:
                    y = 1
                    x = 1
                elif y == 1:
                    y = 0
                    x = 1

    if y == 0:
        picture = claver
    elif y == 1:
        picture = claver2

    cv.imshow("Original image and mask.png", frame+picture)  # In each iterration in the loop it shows the image in real time

    key = cv.waitKey(1)
    if key == 27:
        break

f.close()
cap.release()
cv.destroyAllWindows()


f = open("guru99.txt", "r")             # Opens the txt file end converts the text into speech.
a = f.read()
f.close()
language = 'en'
myobj = gTTS(text=a, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("welcome.mp3")