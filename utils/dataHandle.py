import jieba_fast as jieba
from multiprocessing import Process, Lock, Manager,Pool
import json
import re

import os

#读取所有文本文件的路径
wiki_dirs = []
base_path = 'data/wiki_zh'
for wiki_dir in os.listdir(base_path):
    wiki_dirs.append(os.path.join(base_path, wiki_dir))
#print(wiki_dirs)

data_dirs= []

for wiki_dir in wiki_dirs:
    for data_dir in os.listdir(wiki_dir):
        data_dirs.append(os.path.join(wiki_dir, data_dir))
len(data_dirs)



wiki_list = []
#句子
texts = []

#判断中文
def is_uchar(uchar):
    if uchar >= u'\u4e00' and uchar <=u'\u9fa5':
        return True
    if uchar in ('，','。'):
        return True
    else:
        return False


#读取文件并去除除中文和，。的其他字符
def handle_data(data_dir):
    with open(data_dir,'r') as f:
        wiki_list = []
        for line in f.readlines():
            dic = json.loads(line)
            string = re.sub("[\s+\.\!\/_,$%^*(+\"\'\“\”\【\】\《\》\」\「\·\；\;\:\：]+|[+-！？、~@#￥%……&*（）{}[]()]+".encode('utf-8').decode('utf-8'), "".encode('utf-8').decode('utf-8'),dic.get('text'))
            final_str = ""
            for i in range(len(string)):
                if is_uchar:
                    final_str += string[i]
            # print(final_str)
            wiki_list.append(final_str)
        return wiki_list

print(len(data_dirs))


#分词
def chinese_seg(text):
    word_list = jieba.cut_for_search(text)
    word_list = ','.join(list(word_list))
    return word_list
        

# 分批处理数据
for i in range(0,1200,50):
    wiki_list = []
    #句子
    texts = []
    
    #当前处理文件批序号
    name_index = i
    print("=================================="+str(i)+"===============================")
    
    with Pool(10) as p:
        wiki_list = p.map(handle_data, data_dirs)

    # print("wiki list")
    # print(wiki_list[:1])

    #划分句子
    for wiki_data in wiki_list:
        for wiki in wiki_data:
            for ju in wiki.split('\n'):
                for d in ju.split('。'):
                    if d != '':
                        #print(d.split('，'))
                        for s in d.split('，'):
                            texts.append(s)

    # print('原生句子长度',len(texts))
    # print(texts[:10])
    for text in texts:
        if len(text) <=1:
            texts.remove(text)
    print('移除大小小于1句子长度',len(texts))
     
    
    # print("texts:")
    # print(texts[:10])
    
    #分词
    with Pool(10) as p:
        word_list = p.map(chinese_seg, texts)
    
    # print("word_list 分词")
    # print(word_list[:10])

    #分词后用‘,’组合
    for i in range(len(word_list)):
        words = word_list[i].split(',')
        t = []
        for word in words:
            if len(word) > 1:
                t.append(word)
        word_list[i] = t
    # print("word_list ,")
    # print(word_list[:10])

    
    
    # print('分词后的长度', len(word_list))
    
    #去重词语
    for i in range(len(word_list)):
        word_list[i] = list(set(word_list[i]))
    
    # print("word_list 去重")
    # print(word_list[:10])
    
    #print('修改前')

    #print(word_list[:10])

    # 切割中文词-》中文字
    for i in range(len(word_list)):
        t = []
        for j in range(len(word_list[i])):
            if word_list[i][j] != ' ' or '':
                t += word_list[i][j]
        word_list[i] = t
    # print('修改后')
    # print(word_list[:10])
    
    # ngram
    input_sequences = []
    for line in word_list:
        for i in range(1, len(line)):
            if i > 3:
                break
            n_gram_sequence = line[:i+1]
            input_sequences.append(n_gram_sequence)
            #print(n_gram_sequence)
        
            
    
    # print('ngram')
    # print(input_sequences[:100])
    # print(len(input_sequences))
    

    filename = 'data/wiki_zh_fasttext_2/train_'+str(name_index)+'.txt'
    with open(filename,'w') as f:
        for i in range(len(input_sequences)):
            x = ''.join(input_sequences[i][:-1])
            x1 = ''.join(input_sequences[i][:1])
            y = ''.join(input_sequences[i][-1:])
            y1 = ''.join(input_sequences[i][1:])
            
            f.write(x + '\t__label__' + y + '\n')
            f.write(x1 + '\t__label__' + y1 + '\n')


  