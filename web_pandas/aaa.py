import math

n = 3074
e = 5
num = 1
while (num):
    num = int(input("请输入待加密的数："))
    secret = (num ** e) % n
    print (secret)