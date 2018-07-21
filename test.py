# -*- coding: utf-8 -*-

# 用gensim打开glove词向量需要在向量的开头增加一行：所有的单词数 词向量的维度
import gensim
import os
import shutil
import hashlib
from sys import platform

# 计算行数，就是单词数
def getFileLineNums(filename):
    f = open(filename, 'r')
    count = 0
    for line in f:
        count += 1
    return count


# Linux或者Windows下打开词向量文件，在开始增加一行
def prepend_line(infile, outfile, line):
    with open(infile, 'r') as old:
        with open(outfile, 'w') as new:
            new.write(str(line) + "\n")
            shutil.copyfileobj(old, new)


def prepend_slow(infile, outfile, line):
    with open(infile, 'r') as fin:
        with open(outfile, 'w') as fout:
            fout.write(line + "\n")
            for line in fin:
                fout.write(line)


def load(filename,count):
    num_lines = getFileLineNums(filename)
    gensim_file = 'glove_model.txt'
    gensim_first_line = "{} {}".format(num_lines, count)
    print(gensim_first_line)
    # Prepends the line.
    # if platform == "linux" or platform == "linux2":
    #     prepgensim_first_lineend_line(filename, gensim_file, gensim_first_line)
    # else:
    prepend_slow(filename, gensim_file, gensim_first_line)
    model = gensim.models.KeyedVectors.load_word2vec_format(gensim_file)

    return model



model = load('vectors.txt',10)

word_list = [u'发烧', u'流感']

for word in word_list:
    print word, '--'
    for i in model.most_similar(word, topn=10):
        print i[0], i[1]
    print ''


