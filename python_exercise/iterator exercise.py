def ganZhi():
    #规律为——阳干配阳支，阴干配阴支：
    a = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
    b = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
    c = [a[i%len(a)]+b[i%len(b)]for i in range(60)]
    # 格式化输出，每10个换一行
    for i in range(6):
        print(c[i*10:((i+1)*10)])

    # 结果
    # ['甲子', '乙丑', '丙寅', '丁卯', '戊辰', '己巳', '庚午', '辛未', '壬申', '癸酉']
    # ['甲戌', '乙亥', '丙子', '丁丑', '戊寅', '己卯', '庚辰', '辛巳', '壬午', '癸未']
    # ['甲申', '乙酉', '丙戌', '丁亥', '戊子', '己丑', '庚寅', '辛卯', '壬辰', '癸巳']
    # ['甲午', '乙未', '丙申', '丁酉', '戊戌', '己亥', '庚子', '辛丑', '壬寅', '癸卯']
    # ['甲辰', '乙巳', '丙午', '丁未', '戊申', '己酉', '庚戌', '辛亥', '壬子', '癸丑']
    # ['甲寅', '乙卯', '丙辰', '丁巳', '戊午', '己未', '庚申', '辛酉', '壬戌', '癸亥']

def main():
    ganZhi()

if __name__ == '__main__':
    main()