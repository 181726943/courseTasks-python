import random
n = 52
def gen_pocker(n):
    x = 100
    while(x>0):
        x -= 1
        p1 = random.randint(0,n-1)
        p2 = random.randint(0,n-1)
        t = pocker[p1]
        pocker[p1] = pocker[p2]
        pocker[p2] = t
    return pocker
def get_color(x):
    color = ["梅花","方块","红桃","黑桃"]
    c = int(x / 13)
    if c < 0 or c > 4:
        return "Error!"
    return color[c]
def get_value(x):
    value = x / 13
    if value == 0:
        return 'A'
    elif value >= 1 and value <= 9:
        return str(value + 1)
    elif value == 10:
        return 'J'
    elif value == 11:
        return 'Q'
    elif value == 12:
        return 'K'
def get_Puk(x):
    return get_color(x) + get_value(x)
(a,b,c,d) = ([],[],[],[])
pocker = [i for i in range(n)]
pocker = gen_pocker(n)
print(pocker)
for x in range(13):
    m = x * 4
    a.append(get_Puk(pocker[m]))
    a.append(get_Puk(pocker[m+1]))
    a.append(get_Puk(pocker[m+2]))
    a.append(get_Puk(pocker[m+3]))
a.sort()
b.sort()
c.sort()
d.sort()
print("牌手1:",end=":")
for x in a:
    print(x,end=" ")
    print("\n牌手2:",end=":")
for x in b:
    print(x,end=" ")
    print("\n牌手3:",end=":")
for x in c:
    print(x,end=" ")
    print("\n牌手4:",end=":")
for x in d:
    print(x,end=" ")