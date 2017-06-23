'正则表达式'

import re


def match(reg, src):
    if re.match(reg, src):
        print('match')
    else:
        print('not match')


def testRe():
    # 匹配一个数字、字母或者下划线
    match(r'[0-9a-zA-Z\_]', 'a')
    # 可以匹配至少一个由一个数字、字母、下划线组成的字符串
    match(r'[0-9a-zA-Z\_]', 'a100')
    match(r'[0-9a-zA-Z\_]', '0_z')
    match(r'[0-9a-zA-Z\_]', 'Python3')
    # 匹配由字母或者下划线开头，后接任意数字、字符、下划线组成的字符串
    match(r'[a-zA-Z\_][0-9a-zA-Z\_]*', 'a13823264108')
    # 前面1个字符+后面最多19个字符
    match(r'[a-zA-Z\_][0-9a-zA-Z\_]{0,19}', 'AAAAdsafe')
    # ^以什么开头 ^\w 以字母开头， ^\d以数字开头
    match(r'^\w', 'A00')
    match(r'^\d', '00A')
    # $以什么结束 \d$ 以数字结束 \w$ 以字母结束
    match(r'\d{2}$', '22')
    match(r'\w{3}$', 'AAA')
    match(r'^\d{3}\-\d{3,8}$', '010-12345')
    match(r'^\d{3}\-\d{3,8}$', '010 12345')

    # 切分字符串
    s = re.split(r'[\s\,\;]+', 'a  b c e , ; ce , eaa; aa')
    print(s)

    # 分组
    t = '19:05:30'
    m = re.match(
        r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
    print(m.groups())

    # 正则表达式的贪婪匹配
    print(re.match(r'^(\d+)(0*)$', '102300').groups())
    # 设置为非贪婪匹配
    print(re.match(r'^(\d+?)(0*)$', '102300').groups())

    # 邮箱正则表达式
    match(r'^(\w+\.*\w+)\@(\w+)\.([.\w]+)', 'AC_Dreamer@163.com')
    match(r'^(\w+\.*\w+)\@(\w+)\.([.\w]+)', 'AC_Dreamer@sunet.net.cn')
    match(r'^(\w+\.*\w+)\@(\w+)\.([.\w]+)', 'AC_Dr@eamer@163.com')
    reg = re.match(r'^(\w+\.*\w+)\@(\w+)\.([.\w]+)', 'Cql_liliang@qq.com')
    print(reg.groups())
    reg2 = re.match(
        r'^(\w+\.*\w+)\@(\w+)\.([.\w]+)', 'AC_Dreaemr@sunet.net.cn')
    print(reg2.groups())


if __name__ == '__main__':
    testRe()
