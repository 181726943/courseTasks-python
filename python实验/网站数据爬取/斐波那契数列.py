print("请输入所求数列的项数:",end=" ")
n = int(input())
Fibo = [0,1]
print("斐波那契数列前",n,"项为：")
for i in range(n):
    Fibo.append(Fibo[i] + Fibo[i+1])
    print("Fibo[",i+1,"] = ",Fibo[i],end="\t")
    if i!=0 and (i+1) % 5 == 0:
        print()