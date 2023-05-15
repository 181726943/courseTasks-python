import random
x = random. randrange(100,201)
print(x,end=" ")
MAX = x
for i in range (2,11):
    x = random. randrange(100,201)
    print(x,end=" ")
    if MAX < x:
        MAX = x
print("max = ",MAX)