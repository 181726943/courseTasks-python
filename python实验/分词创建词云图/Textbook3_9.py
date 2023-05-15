i = 1
e = 1
plus = 1
temp = 1 / plus
while temp > 10 ** (-5):
    plus *= i
    temp = 1 / plus
    e += temp
    i += 1
print("e = ",e)