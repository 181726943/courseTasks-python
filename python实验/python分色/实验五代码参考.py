import imutils
from cv2 import cv2
import numpy as np
font=cv2.FONT_HERSHEY_COMPLEX
imgpath=r'test.jpg'
image = cv2.imread(imgpath)
b = image.shape
cy = np.zeros(list(b[:2]))
# cv2.imshow('image',image)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  # 色彩空间转换为hsv，便于分离
lower_hsv = np.array([35, 128, 46])          # 提取颜色的低值
high_hsv = np.array([77, 255, 255])          # 提取颜色的高值

mask = cv2.inRange(hsv, lowerb=lower_hsv, upperb=high_hsv)
# cv2.imshow('red',mask)

blurred = cv2.GaussianBlur(mask, (9, 9), 0)
ret,th1=cv2.threshold(blurred,110,255,cv2.THRESH_BINARY)
# cv2.imshow("th1",th1)

BlueThings = cv2.bitwise_and(image, image,  mask=th1)
# cv2.imshow('BlueThings',BlueThings)

result = BlueThings
# write result to disk
cv2.imwrite("soccer_floodfill.jpg", result)

result1 = cv2.imread("soccer_floodfill.jpg")
h, w, c = result1.shape
print(h,w,c)

hsv1 = cv2.cvtColor(result1,cv2.COLOR_BGR2HSV)
lower_red= np.array([0,0,0])
upper_red = np.array([180,255,46])
mask1 = cv2.inRange(hsv1, lower_red, upper_red)
# cv2.imshow("mask1",mask1)

erode=cv2.erode(mask1,None,iterations=1)#腐蚀
#cv2.imshow('erode',erode)
dilate=cv2.dilate(erode,None,iterations=1)#膨胀
#cv2.imshow('dilate',dilate)

for i in range(h):
  for j in range(w):
    if dilate[i,j]==255:    #像素点255表示白色
      result1[i,j]=(255,255,255)  # 此处替换颜色，为BGR通道，不是RGB通道
# cv2.imshow('edged',result1)

edged = cv2.Canny(th1, 60, 150)

cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

total = 0
Circleshape,Threeshape,Foreshape = 0,0,0

# loop over the contours one by one
for c in cnts:
    # if the contour area is small, then the area is likely noise, so
    # we should ignore the contour
    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x)+int(radius),int(y))
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    # 如果当前的轮廓含有3个顶点，则其为三角形
    if len(approx) == 3:
        Threeshape =  Threeshape + 1
        result=cv2.putText(result1,'Three'+str(Threeshape),center,font,0.5,(0,0,0))
        

    # 如果当前的轮廓含有4个顶点，则其可能是矩形或者正方形
    elif len(approx) == 4:
        Foreshape =  Foreshape + 1
        result=cv2.putText(result1,'Fore'+str(Foreshape),center,font,0.5,(0,0,0))
    else:
        Circleshape =Circleshape + 1
        result=cv2.putText(result1,'Circle'+str(Circleshape),center,font,0.5,(0,0,0))
        # otherwise, draw the contour on the image and increment the total
        # number of shapes found
        #cv2.drawContours(image, [c], -1, (204, 0, 255), 2)
    total += 1 
# show the output image and the final shape count
info="[INFO] found {} Red shapes".format(total)
a1="[INFO] found {} Circleshape".format(Circleshape)
a2="[INFO] found {} Threeshape".format(Threeshape)
a3="[INFO] found {} Foreshape".format(Foreshape)

result=cv2.putText(result1,info,(700,40),font,0.5,(0,255,10))
result=cv2.putText(result1,a1,(700,60),font,0.5,(0,255,10))
result=cv2.putText(result1,a2,(700,80),font,0.5,(0,255,10))
result=cv2.putText(result1,a3,(700,100),font,0.5,(0,255,10))


print("[INFO] found {} Red shapes".format(total))
print("[INFO] found {} Circleshape".format(Circleshape))
print("[INFO] found {} Threeshape".format(Threeshape))
print("[INFO] found {} Foreshape".format(Foreshape))


cv2.imshow("Image1", result1)
cv2.waitKey(0)
cv2.destroyAllWindows()
