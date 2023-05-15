def main():
    file=open("E:\\桌面\\LSZdocuments\\Python课程实验报告\\Python作业任务二\\Eugenie Grandet - Honore de Balzac.txt",'r')
    wordCounts={}    #先建立一个空的字典，用来存储单词 和相应出现的频次
    for line in file:
        lineprocess(line.lower(),wordCounts)  #对于每一行都进行处理，调用lineprocess()函数，参数就是从file文件读取的一行
        items0=list(wordCounts.items())       #把字典中的键值对存成列表，形如：["word":"data"]
        items=[[x,y] for (y,x) in items0]     #将列表中的键值对换一下顺序，方便进行单词频次的排序 就变成了["data":"word"]
        items.sort()            #sort()函数对每个单词出现的频次按从小到大进行排序


    statis = open("E:\\pythonFiles\\lessonExperiments\\第二次作业\\统计结果.txt",'w')
    statis.write("单词\t\t频率\n")
    counter = len(items)
    for i in range(counter-1,0,-1):   #上一步进行排序之后 对items中的元素从后面开始遍历 也就是先访问频次多的单词
        statis.write(items[i][1]+"\t\t"+str(items[i][0])+"\n")
    print("出现频次最多的20个单词为：")
    for i in range(counter-1,counter-40,-2):
        print(items[i][1])




def lineprocess(line,wordCounts):
    for ch in line:   #对于每一行中的每一个字符 对于其中的特殊字符需要进行替换操作
        if ch in "~@#$%^&*()_-+=<>?/‘“’”,.:!;{}[]|\"":
            line=line.replace(ch," ")
    words=line.split()  #替换掉特殊字符以后 对每一行去掉空行操作,也就是每一行实际的单词数量
    for word in words:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            wordCounts[word]=1    

    #这个函数执行完成之后整篇文章里每个单词出现的频次都已经统计好了


main()