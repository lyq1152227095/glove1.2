# glove
cutword.py ：使用jieba分词进行中文文件分词。
斯坦福的glove只能进行词向量生成，而且对词有一定的要求，如不能含有标点符号。
使用glove的标准流程是：
1.数据清洗，洗掉脏数据，如标点，无效字符，这部分需要自己根据需求进行清洗。
2.中文分词，本项目使用jieba分词，分词结果保存在文件“fenci”中。
3.词向量生成，执行demo.sh。
「
CORPUS=fenci（你的分词后的文件作为输入）
VOCAB_FILE=vocab.txt（词频统计输出，不需要修改）
COOCCURRENCE_FILE=cooccurrence.bin
COOCCURRENCE_SHUF_FILE=cooccurrence.shuf.bin
BUILDDIR=build
SAVE_FILE=vectors （词向量输出文件，一般不用修改）
VERBOSE=2 
MEMORY=4.0 
VOCAB_MIN_COUNT=5 （词频统计中最小词频）
VECTOR_SIZE=10 （词向量的大小，根据需求进行修改）
MAX_ITER=15 （最大训练次数）
WINDOW_SIZE=5 （词共现矩阵统计时窗口的大小）
BINARY=2 
NUM_THREADS=8
X_MAX=10
」
4.词向量调用和测试，执行test.py，利用gensim模块进行加载模型，glov训练出来的词向量比word2vec训练处理啊的少了第一行（词的个数，向量维度），在test.py中添加了这一行，其他的和word2vec一样。

注意：
1.在执行demo.sh时可能会有一个报错，是python执行的问题，不用理会。
2.执行训练时，数据少，训练次数多或导致loss变成none，可以调整MAX_ITER（有人说感觉斯坦福的算法中的梯度下降有问题才导致的出现none，不过本人感觉没什么问题）。



