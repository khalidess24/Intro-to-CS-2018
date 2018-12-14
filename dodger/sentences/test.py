import os

path = os.getcwd()
sentencelist = os.listdir(path)




sentencelist.remove('.DS_Store')
sentencelist.remove('test.py')
# print(sentencelist.index('test.py'))

# print(sentencelist)


sentences = []
for i in sentencelist:
    city = open(path+"/"+i,'r') #encoding='utf-8'
    for line in city:
        x = line.rstrip().split(",")
        sentences.append({x[0]:x[1]})

print(sentences[0])
