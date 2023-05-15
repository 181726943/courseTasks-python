# 导入python包
import numpy as np
import imutils
from cv2 import cv2

font=cv2.FONT_HERSHEY_COMPLEX

def color_seperate(img,min,max,color):
    ##将BGR图像转化为HSV图像，方便颜色分离
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_hsv = np.array([min,43,46])
    high_hsv = np.array([max,255,255])
    mask = cv2.inRange(hsv,lowerb = lower_hsv,upperb = high_hsv)

    blurred = cv2.GaussianBlur(mask, (9, 9), 0) #高斯模糊
    _,th1=cv2.threshold(blurred,110,255,cv2.THRESH_BINARY) #阈值分割

    colors = cv2.bitwise_and(img, img,  mask=th1)  #对图像（灰度图像或彩色图像均可）
                                                   #每个像素值进行二进制“与”操作

    result = colors
    cv2.imwrite(color+'.jpg',result)
    result1 = cv2.imread(color+'.jpg')

    h,w,_ = result1.shape

    hsv1 = cv2.cvtColor(result1,cv2.COLOR_BGR2HSV)
    lower_red= np.array([0,0,0])
    upper_red = np.array([180,255,46])
    mask1 = cv2.inRange(hsv1, lower_red, upper_red)

    erode=cv2.erode(mask1,None,iterations=1)#腐蚀
    #cv2.imshow('erode',erode)
    dilate=cv2.dilate(erode,None,iterations=1)#膨胀
    #cv2.imshow('dilate',dilate)

    ##将图片背景换成白色
    for i in range(h):
        for j in range(w):
            if dilate[i,j]==255:    #像素点255表示白色
                result1[i,j]=(255,255,255)  # 此处替换颜色，为BGR通道，不是RGB通道
    # cv2.imshow('edged',result1)


    # cv2.imshow("ginRange",mask)
    # mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(th1,60,150) #边缘检测

    cnts = cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    all_graph = 0
    triangle,rect = 0,0
    for c in cnts:
        (x,y),radius = cv2.minEnclosingCircle(c)
        center = (int(x)+int(radius),int(y))
        peri = cv2.arcLength(c,True) #计算周长
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 3:
            triangle += 1
            result = cv2.putText(result1, 'trangle' + str(triangle), center, font,0.5,(255,0,0))
        elif len(approx) == 4:
            rect += 1
            result = cv2.putText(result1, 'retcangle' + str(rect), center,font,0.5,(255,0,0))
        all_graph += 1
    info="[INFO] found "+str(color)+str(all_graph)+"shapes"
    a2="[INFO] found {} Threeshape".format(triangle)
    a3="[INFO] found {} Foreshape".format(rect)

    result=cv2.putText(result1,info,(700,60),font,0.5,(0,255,10))
    result=cv2.putText(result1,a2,(700,80),font,0.5,(0,255,10))
    result=cv2.putText(result1,a3,(700,100),font,0.5,(0,255,10))
    
    cv2.imwrite(str(color)+".jpg",result)

    print("[INFO] found {} "+str(color),all_graph,"shapes")
    print("[INFO] found {} Threeshape".format(triangle))
    print("[INFO] found {} Foreshape".format(rect))

    ##展示结果
    cv2.imshow("Image1", result1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image = cv2.imread('test.jpg')
color_seperate(image,156,180,"red") # 红色图形检测
color_seperate(image,35,77,"green") # 绿色图形检测
color_seperate(image,78,124,'blue') # 蓝色图形检测

