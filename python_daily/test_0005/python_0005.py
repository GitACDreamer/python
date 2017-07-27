# E:\Programs\Python\python_daily
'统计文本中英文单词的个数'

import re


def countWords():
    try:
        dictw = {}
        cnt = 0
        with open(r'E:\Programs\Python\python_daily\test_0005\test_0005.txt', 'r') as f:
            for line in f.readlines():
                # 用正则表达式分割字符串
                oldWords = re.split('\W+', line)
                newWords = [x for x in oldWords if x != '']

                # 用dict类型保存每个单词出现的次数
                for word in newWords:
                    if word in dictw:
                        dictw[word] += 1
                    else:
                        dictw[word] = 1
                    cnt = cnt + 1

            # 将单词出现的次数按逆序排序
            dictw = sorted(dictw.items(), key=lambda x: x[1], reverse=True)

            # 单词总数
            print('单词总数是：%d' % cnt)
            # 打印出统计结果
            for k, v in dictw:
                print(k, ': ', v)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    countWords()
