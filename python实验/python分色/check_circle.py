# 导入python包
import numpy as np
import imutils
from cv2 import cv2

##首先获取图像
g_image = cv2.imread("green.jpg")#绿色圆
r_image = cv2.imread("red.jpg")#红色圆
b_image = cv2.imread("blue.jpg")#蓝色圆


##将图片灰度化
g_gray_img = cv2.cvtColor(g_image,cv2.COLOR_BGR2GRAY)
r_gray_img = cv2.cvtColor(r_image,cv2.COLOR_BGR2GRAY)
b_gray_img = cv2.cvtColor(b_image,cv2.COLOR_BGR2GRAY)

##滤波降噪,方便进行霍夫圆检测
##霍夫变换通常情况下受图片的噪声信息干扰非常大，所以通常情况下我们需要对图像进行预处理操作
g_img = cv2.medianBlur(g_gray_img, 7)  #进行中值模糊，去噪点
g_img = cv2.GaussianBlur(g_img,(17,19),0) #高斯模糊

r_img = cv2.medianBlur(r_gray_img, 1)  #进行中值模糊，去噪点
r_img = cv2.GaussianBlur(r_img,(17,21),0) #高斯模糊

b_img = cv2.medianBlur(b_gray_img, 7)  #进行中值模糊，去噪点
b_img = cv2.GaussianBlur(b_img,(17,19),0) #高斯模糊



# 霍夫变换圆检测
gcircles= cv2.HoughCircles(g_img,cv2.HOUGH_GRADIENT,dp=1,minDist=65,param1=50,param2=30,minRadius=5,maxRadius=750)
rcircles= cv2.HoughCircles(r_img,cv2.HOUGH_GRADIENT,dp=1,minDist=65,param1=50,param2=30,minRadius=5,maxRadius=750)
bcircles= cv2.HoughCircles(b_img,cv2.HOUGH_GRADIENT,dp=1,minDist=65,param1=50,param2=30,minRadius=5,maxRadius=750)

#gcircles = np.uint16(np.around(gcircles)) #把circles包含的圆心和半径的值变成整数

#print(type(gcircles))

# 输出返回值，方便查看类型
# print(gcircles)
# print(gcircles[0])

# 输出检测到圆的个数
#print(len(gcircles[0]))

##创建一个绘制绿色圆的图像，968X970大小，数据类型无符号8位
green_cir = np.ones((968,970,3),np.uint8)
#将底片转换为白色
green_cir[:,:,0] = 255
green_cir[:,:,1] = 255
green_cir[:,:,2] = 255

##gcounter用于统计圆的个数
gcounter = 0
# 根据检测到绿色圆的信息，画出每一个圆
for circle in gcircles[0]:
    gcounter += 1
    # 圆的基本信息(半径)
    # print(circle[2])
    # 坐标行列
    x = int(circle[0])
    y = int(circle[1])
    # 半径
    r = int(circle[2])
    # 在原图用指定颜色标记出圆的位置
    g_img = cv2.circle(green_cir, (x, y), r, (36, 223, 204), -1)
    #g_img = cv2.circle(g_img, (x, y), 2, (35, 43, 46), -1)#打印圆心

    #设置参数——绘制的文字，位置，字型，字体大小，文字颜色，线型
    font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(g_img,"circle"+str(gcounter),(x - r, y - r), font, 0.8,(0,0,0),2)

# 显示新图像
# cv2.imshow('green', g_img)
cv2.imwrite("green_circle.jpg",g_img)



##创建一个绘制红色圆的图像，968X970大小，数据类型无符号8位
red_cir = np.ones((968,970,3),np.uint8)
#将底片转换为白色
red_cir[:,:,0] = 255
red_cir[:,:,1] = 255
red_cir[:,:,2] = 255

rcounter = 0
# 根据检测到红色圆的信息，画出每一个圆
for circle in rcircles[0]:
    rcounter += 1
    # 圆的基本信息(半径)
    #print(circle[2])
    # 坐标行列
    x = int(circle[0])
    y = int(circle[1])
    # 半径
    r = int(circle[2])
    # 在原图用指定颜色标记出圆的位置
    r_img = cv2.circle(red_cir, (x, y), r, (0, 0, 255), -1)

    #设置参数——绘制的文字，位置，字型，字体大小，文字颜色，线型
    font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(r_img,"circle"+str(rcounter),(x - r, y - r - 20), font, 0.8,(0,0,0),2)

# r_img = cv2.blur(r_img, (2,2))#均值滤波处理
# r_img = cv2.medianBlur(r_img,3)#中值滤波处理
##实验证明下面两个结合处理效果更好 
r_img = cv2.GaussianBlur(r_img , (3,3) ,0)#高斯滤波处理
r_img = cv2.bilateralFilter(r_img, 9, 80, 80)#双边滤波处理

# 显示新图像
cv2.imshow('red', r_img)
cv2.imwrite("red_circle.jpg",r_img)



##创建一个绘制蓝色圆的图像，968X970大小，数据类型无符号8位
blue_cir = np.ones((968,970,3),np.uint8)
#将底片转换为白色
blue_cir[:,:,0] = 255
blue_cir[:,:,1] = 255
blue_cir[:,:,2] = 255

bcounter = 0
# 根据检测到蓝色圆的信息，画出每一个圆
for circle in bcircles[0]:
    bcounter += 1
    # 圆的基本信息(半径)
    #print(circle[2])
    # 坐标行列
    x = int(circle[0])
    y = int(circle[1])
    # 半径
    r = int(circle[2])
    # 在原图用指定颜色标记出圆的位置
    b_img = cv2.circle(blue_cir, (x, y), r, (240, 139, 28), -1)

    #设置参数——绘制的文字，位置，字型，字体大小，文字颜色，线型
    font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    cv2.putText(b_img,"circle"+str(bcounter),(x - r, y - r), font, 0.8,(0,0,0),2)

# 显示新图像
# cv2.imshow('blue', b_img)
cv2.imwrite("blue_circle.jpg",b_img)




cv2.waitKey(0)
cv2.destroyAllWindows()
