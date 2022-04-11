import cv2 as cv
import numpy as np
import math
mid = []
def averager(points):
    sumX = 0
    total = len(points[0])
    for i in points[0]:
        sumX += i
    if(total):
        return sumX//total
    else:
        return 0

def loopingthingy(heightener, left = True):
    for n in range(4, 10): # isnt this like a riemman's sum idk i dont pay attention in calc
        if left:
           x = lastX -heightener * n
        else:
            x = lastX + heightener * n
        topy = 0
        bottomy = 0
        for y in range(height):
            if (binary[y][x] == 200):
                topy = y
                break
        for y in range(height):
            if (binary[height - y][x] == 200):
                bottomy = height - y
                break
        mids = (topy + bottomy) // 2
        mid.append((x, mids))

def splitinttwo(points, axis):
    left = []
    right = []
    if axis == 'x':
        average = averager(points)
        for i in points[0]:
            if i < average:
                left.append(i)
            else:
                right.append(i)
    else:
        average = averager(points[1])
        for i in points[0]:
            if i < average:
                left.append(i)
            else:
                right.append(i)
    return left, right

img = cv.imread("flipedphoto2.jpg")
scale_percent = 20
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
height -=50
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
dst = cv.Canny(gray, 75, 300)
blur = cv.blur(dst, (10,10))
n = 10
heightOfBox = height//n

bruhbrobruh, binary = cv.threshold(blur, 50, 200, cv.THRESH_BINARY)

for ididntthinkineededthis in range(7):#originally didnt think i would use that value
    y = height-ididntthinkineededthis*heightOfBox -1 #it was giving me some sort of error with index so i just sub 1
    left, right = splitinttwo(np.where(binary[y] == 200), "x")
    if len(left) and len(right):
        midX = (left[0]+right[0])//2
    else:
        midX= 0
    mid.append((midX, y))

for i in mid:
    cv.circle(img, i, 3, (0, 0, 0), -1)

dir = mid[-2][0]-mid[-1][0]
lastX = mid[-1][0]
lastY = mid[-1][1]
heightener = (width - lastX) // 10

if(dir < 0): #code for right side
    loopingthingy(heightener, False)
else:
    loopingthingy(heightener, True)


curr = 0
for i in mid:
    if curr<len(mid)-1:
        cv.arrowedLine(img, i, mid[curr+1], (255,0,255), 2)
    curr+=1

cv.imshow('bruh3', img)
cv.waitKey()
