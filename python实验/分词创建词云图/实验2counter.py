from collections import defaultdict, Counter


def getText():
    txt = open("Eugenie Grandet - Honore de Balzac.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~':
        txt = txt.replace(ch, " ")
    return txt


def func_counter(word_list):
    """
    方法之一：使用Counter 本例子

    
    还可以使用nltk的FreqDist
    count_result = FreqDist(samples=wordlist)
    return dict(count_result.most_common()) if fmt == 'dict' else count_result.most_common()
 
    jieba分词统计
    with open("origin_data/weibo.txt", 'r') as f:
        texts = f.read()  # 读取整个文件作为一个字符串
        result = analyse.textrank(texts, withWeight=True)  # textrank算法排序
        # result = analyse.extract_tags(sentence=texts, withWeight=True)  # tfidf考虑权重
        print(result)
    
    使用pandas的value_counts
    count_result = pd.Series(words).value_counts()
    return count_result.to_dict()
    
    使用defaultdict
    count_dict = defaultdict(lambda: 0)
    for item in word_list:
        count_dict[item] += 1
    return sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
 

    方法：使用字典
      
    count_dict = {}
    for item in word_list:
        count_dict[item] = count_dict[item] + 1 if item in count_dict else 1
    return sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    """
    count_result = Counter(word_list)
    # print(count_result)   # 一个字典对象
    # print(count_result.keys())   # 一个字典key值
    # print(count_result.values())   # 一个字典value值
    # print(list(count_result.elements()))  # 返回的是 word_list
    # print(count_result.most_common(3))
    return count_result



hamletTxt = getText()
words = hamletTxt.split()


result = func_counter(words)

outers=result.most_common(20)
for i in  outers:
    word, count = i[0], i[1]
    print("{0:<10}{1:<5}".format(word, count))

