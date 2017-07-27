'当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights'
filters = set()

def fileterWords():
    try:
        with open('test_0012.txt' , 'r' , -1 , encoding='utf8') as f:
            for line in f.readlines():
                filters.add(line.rstrip('\n'))
        while True:
            s = input('请输入字符：')
            if s == 'exit':
                break
            elif s in filters:
                print('Freedom')
            else:
                print('Human Rights')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    fileterWords()