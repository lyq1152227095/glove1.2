import jieba
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
seqall =[]
fencijieguo = []
def shucu(seq):
    for i in range(len(seq)):
        print(seq[i].decode('utf-8'))

with open('zhongwen.txt','r') as f:
    for line in f:
        seqall.append(line.strip())

print("start cut")
for i in range(len(seqall)):
    fencijieguo.append([' '.join(list(jieba.cut(seqall[i])))])
    if i%100==0:
        print(i)

with open("fenci",'wb') as fw:
    for i in range(len(fencijieguo)):
        fw.write(fencijieguo[i][0].encode("utf-8"))
        fw.write('\n')





