'第三方库Pillow'

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random


def testResizeImage():
    # 打开一张图片
    im = Image.open('test_zippng.png')
    # 获取图片尺寸大小
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    # 缩放50%
    im.thumbnail((w / 2, h / 2))
    print('Resize image to: %sx%s' % (w // 2, h // 2))
    # 保存图片
    im.save('test_zippng_resize.png', 'png')
    im.show()


def testFilterImage():
    # 打开一张图片
    im = Image.open('test.jpg')
    # 模糊图片
    im.filter(ImageFilter.GaussianBlur)
    im.save('test_blur.jpg', 'jpeg')
    # 显示图片
    im.show()


def randomChar():
    return chr(random.randint(65, 90))


def randomTextColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def randomBgColor():
    return (random.randint(32, 137), random.randint(32, 137), random.randint(32, 137))


def testDrawImage():
    width = 240
    height = 60
    # 创建一张240*60的图片
    im = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建font对象
    font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 36)
    # 创建draw对象
    draw = ImageDraw.Draw(im)

    # 填充图片
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=randomBgColor())
    # 输出文字
    for t in range(4):
        draw.text((60 * t + 10, 10), randomChar(),
                  fill=randomTextColor(), font=font)

    # 模糊图片
    im.filter(ImageFilter.BLUR)
    im.save('code.jpg', 'jpeg')
    im.show()


if __name__ == '__main__':
    # testResizeImage()
    # testFilterImage()
    testDrawImage()
