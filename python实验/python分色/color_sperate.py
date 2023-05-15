from cv2 import cv2
import numpy as np



def separate_green(frame):
    cv2.imshow("原图",frame)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([35,43,46])
    high_hsv = np.array([77,255,255])
    mask = cv2.inRange(hsv,lowerb = lower_hsv,upperb = high_hsv)

    blurred = cv2.GaussianBlur(mask, (17, 19), 0)
    _,th1=cv2.threshold(blurred,110,255,cv2.THRESH_BINARY)

    # cv2.imshow("ginRange",mask)
    # mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    return th1


def separate_red(frame):
    cv2.imshow("原图",frame)

    ##膨胀操作
    kernel = np.ones((5,5), np.uint8)
    frame = cv2.dilate(frame,kernel,iterations=1)

    # cv2.imshow("blur",frame)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([156,43,46])
    high_hsv = np.array([180,255,255])
    mask = cv2.inRange(hsv,lowerb = lower_hsv,upperb = high_hsv)

    ##腐蚀操作
    # mask = cv2.erode(mask, kernel)

    mask = cv2.dilate(mask,kernel,iterations = 1)


    # mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("rinRange",mask)
    return mask


def separate_blue(frame):
    cv2.imshow("原图",frame)
    # se = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 19), (-1, -1))
    # frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, se)
    ##膨胀操作
    kernel = np.ones((5,5), np.uint8)
    frame = cv2.erode(frame,kernel,iterations=1)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([78,43,46])
    high_hsv = np.array([124,255,255])
    mask = cv2.inRange(hsv,lowerb = lower_hsv,upperb = high_hsv)

    mask = cv2.erode(mask, kernel)#腐蚀操作

    # mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
    # cv2.imshow("binRange",mask)
    return mask


color_image = "test.jpg"
src_color = cv2.imread(color_image)


##分离绿色圆
cv2.imwrite("green1.jpg",separate_green(src_color))

#分离红色圆
cv2.imwrite("red1.jpg",separate_red(src_color))

##分离蓝色圆
cv2.imwrite("blue1.jpg",separate_blue(src_color))

cv2.waitKey(0)
cv2.destroyAllWindows()