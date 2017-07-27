'读取某个目录下的所有文章，统计每篇文章最重要的单词'

import os
import re


def countImportantWords():
    try:
        filepath = r'E:\Programs\Python\python_daily\test_0007'
        # 保存每个文件最重要的单词
        dict_most_words = {}
        # 保存最重要单词出现的次数
        dict_most_words_count = {}

        # 遍历test_0007目录下所有文件
        for file in os.listdir(filepath):
            dictw = {}
            # 打开test_0007目录下的某一个文件
            with open(filepath + '\\' + file) as f:
                # 读文件的一行
                for line in f.readlines():
                    # 按单词分割
                    oldWords = re.split('\W+', line)
                    # 去掉空字符串
                    newWords = [x for x in oldWords if x != '']
                    # 统计单词出现的次数
                    for word in newWords:
                        if word in dictw:
                            dictw[word] += 1
                        else:
                            dictw[word] = 1
                # 将某一文件中的字符串按频率高到低排序(返回的结果是是一个list不是dict)
                dictw = sorted(dictw.items(), key=lambda x: x[1], reverse=True)
                if len(dictw) > 0:
                    for k, v in dictw:
                        # 将每个文件单词出现次数最多的保存下来
                        dict_most_words[file] = k
                        dict_most_words_count[file] = v
                        break
                else:
                    print('当前文件为空')
        for k, v in dict_most_words.items():
            print('文件%s最重要的单词是：%s，出现%d次' % (k, v, dict_most_words_count[k]))
    except IOError as e:
        print(e)

if __name__ == '__main__':
    countImportantWords()
