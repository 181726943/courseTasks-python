import pandas as pd
listSer = pd.Series([1,1,1,2,5,26,1,3,2,62,34,6,9,2,\
                     23,8,45,23,3,1,2]).value_counts()#统计列表中每个元素出现的次数
lists = listSer.to_dict()
word = list(lists.keys())
words = lists.keys()
print(listSer)
print(lists)
print(words)
for i in words:
    print(lists[i])
