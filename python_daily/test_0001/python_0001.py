# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def write_number(image_file_path, number=10):
    img = Image.open(image_file_path)
    font_size = img.size[0] if img.size[0] < img.size[1] else img.size[1]
    font_size = int(font_size / 4)
    number_txt = str(number) + ' ' if number < 100 else '99+'
    font = ImageFont.truetype(r'C:\Windows\Fonts\consola.ttf', size=font_size)
    if font.getsize(number_txt)[0] > img.size[0] or font.getsize(number_txt)[1] > img.size[1]:
        return img
    position = img.size[0] - font.getsize(number_txt)[0]
    ImageDraw.Draw(img).text((position, 0), number_txt, (255, 0, 0), font)
    img.show()
    return img


if __name__ == '__main__':
    # need an image '0000.png'
    write_number(r'E:\Programs\Python\python_daily\test_0001\p0001.jpg').save(
        r'E:\Programs\Python\python_daily\test_0001\p0001_r.jpg')
    # if number > 100, shows '99+'
    write_number(r'E:\Programs\Python\python_daily\test_0001\p0001.jpg', 100).save(
        r'E:\Programs\Python\python_daily\test_0001\p0001_r100.jpg')
