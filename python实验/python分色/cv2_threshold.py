#! usr/bin/env python
# coding: utf-8
from cv2 import cv2

img = cv2.imread('test.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 先将图像矩阵进行二值化
# img = cv2.imread('cat.jpg'，0)
# 也可以直接将图像用灰度值读入，其中0就表示用灰度读图

cv2.imshow('img',img)

_,img1 = cv2.threshold(img,100,250,cv2.THRESH_BINARY)
# 这个函数返回两个值，第二个值才是二值化后的图像矩阵
# 最后一个参数表示一种二值化算法
# 阈值设置为100,
# 250表示大于100的像素值会被重新赋值为250

cv2.imshow('img',img1)

# cv2.waitKey()
cv2.destroyAllWindows()


############ 以下比较不同简单二值化算法的区别

# 先进行不同算法的二值化
ret,img1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# 从名字可以看出一点来，binary是二元的意思，这里指要么0，要么指定的一个值（255）
print(ret)
ret,img2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
# 注意到INV表示逆，全写是inverse
ret,img3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
# 注意到truncate表示截断的意思。这个函数不再是二元，而是对超过某个值的部分进行处理，否则并不会处理。
ret,img4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
# 实际上，这也是一种阶段，对大于某一个值的像素值进行调整，与trunc不同的是，这里变为0，而不是最大值
ret,img5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

import numpy as np
import matplotlib.pyplot as plt
#用这个模块来画图显示，这个库和opencv有些不同，可参考前面的博客
# https://blog.csdn.net/qq_27261889/article/details/80543966

# 先定义以下图的图题和图像矩阵
titles = ['original','binary','binary_inv','trunc','tozero','tozero_inv']
imgs = [img,img1,img2,img3,img4,img5]

for i in range(6):
    plt.subplot(2,3,i+1)#分别画出每一个图
    plt.imshow(imgs[i],'gray')
    plt.title(titles[i])#写出图题

plt.show()