from PIL import Image

def zipImage():
    im = Image.open('E:\\Programs\\Python\\test_zippng.png')
    print(im.format , im.size , im.mode)
    im.thumbnail((100,100))
    im.show()
    im.save('zipped.png', 'PNG')
def main():
    zipImage() 

if __name__ == '__main__':
    main()