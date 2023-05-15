from collections import defaultdict, Counter
import pandas as pd


def getText():
    txt = open("Eugenie Grandet - Honore de Balzac.txt", "r").read()#读取文档，
    txt = txt.lower()              #将文档中的字母全部转化为小写
    for ch in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~':     #除去特殊字符：用空格代替特殊字符
        txt = txt.replace(ch, ' ')
    return txt


def func_counter(word_list):        #用pandas包中的方法统计文档中的单词数
    count_result = pd.Series(words).value_counts() #统计单词出现的频率
    return count_result.to_dict()    #将统计结果包装成字典
    # print(count_result)   # 一个字典对象
    # print(count_result.keys())   # 一个字典key值
    # print(count_result.values())   # 一个字典value值
    # print(list(count_result.elements()))  # 返回的是 word_list
    # print(count_result.most_common(3))
    # count_result = Counter(word_list)
    # return count_result

hamletTxt = getText()
words = hamletTxt.split()    #替换掉特殊字符以后 对每一行去掉空行操作,也就是每一行实际的单词数量
result = func_counter(words)

#将统计到的单词及频率写入文档
word = list(result.keys())   #将字典中的键存入列表
tatis = open("统计数据.txt",'w')#创建文件
tatis.write("单词\t\t频率\n")
for i in word:    #写入文件统计结果
    strs = str(result[i])
    tatis.write(i+"\t\t"+strs+"\n")

#统计出现频率最高的20个单词
print("出现频率最高的20个单词如下")
for counts in range(20):
    print(word[counts],end=" ")
print("\n")

#统计不同频率阶段单词数
datas = list(result.values())
length = len(datas)
count1 = 0
count2 = 0
count3 = 0
count5 = 0
count10 = 0
count20 = 0
count30 = 0
count50 = 0
count100 = 0
count500 = 0
for num in range(length):
    if datas[num] >= 500:
        count500 += 1
    elif datas[num] >= 100:
        count100 += 1
    elif datas[num] >= 50:
        count50 += 1
    elif datas[num] >= 30:
        count30 += 1
    elif datas[num] >= 20:
        count20 += 1
    elif datas[num] >= 10:
        count10 += 1
    elif datas[num] >= 5:
        count5 += 1
    elif datas[num] >= 3:
        count3 += 1
    elif datas[num] >= 2:
        count2 += 1
    else :
        count1 += 1
print("出现500次以上的单词，",count500)
print("出现100次以上的单词，",count100)
print("出现50次以上的单词，",count50)
print("出现30次以上的单词，",count30)
print("出现20次以上的单词，",count20)
print("出现10次以上的单词，",count10)
print("出现5次以上的单词，",count5)
print("出现3次以上的单词，",count3)
print("出现2次以上的单词，",count2)
print("出现1次以上的单词，",count1)





#word_list = list(result.items())
#outers=len(word_list)
#statis = open("E:\\pythonFiles\\lessonExperiments\\第二次作业\\统计.txt",'w')
#for i in range(outers):
    #word, count = word_list[i][0],word_list[i][1]
    #statis.write("{0:<10}{1:<5}\n".format(word, count))