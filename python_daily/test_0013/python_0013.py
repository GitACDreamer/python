'当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights'
filters = set()

def fileterWords():
    try:
        with open(r'E:\Programs\Python\python_daily\test_0013\test_0013.txt', 'r', -1, encoding='utf8') as f:
            for line in f.readlines():
                filters.add(line.rstrip('\n'))
        while True:
            s = input('请输入字符：')
            if s == 'exit':
                break
            else:
                for it in filters:
                    if it in s:
                        # 将敏感字符用同样数量的*替代
                        s = s.replace(it, '*' * len(it))
                print(s)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    fileterWords()
