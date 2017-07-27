'生成字母验证码的图片'

__author__ = 'Leland'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

IMAGE_MODE = 'RGB'
IMAGE_BG_COLOR = (255, 255, 255)
IMAGE_FONT = r'C:\Windows\Fonts\Arial.ttf'
text = ''.join(random.sample(
    'abcdefghijklmnopqrstuvwxwz\ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))


def color_bg_random():
    """随机颜色"""
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def color_text_random():
    return (random.randint(64, 220), random.randint(64, 220), random.randint(64, 220))


def draw_image(strs, width=400, height=200, chance=2):
    # strs 验证码内容
    # width 图片宽度
    # height 图片高度
    # chance 噪点频率(%)

    # 创建图片
    im = Image.new(IMAGE_MODE, (width, height), IMAGE_BG_COLOR)
    # 创建draw
    draw = ImageDraw.Draw(im)
    # 绘制背景噪点
    for w in range(width):
        for h in range(height):
            if chance < random.randint(1, 100):
                draw.point((w, h), fill=color_bg_random())
    # 创建字体
    font = ImageFont.truetype(IMAGE_FONT, 120)
    fw, fh = font.getsize(strs)
    x = (width - fw) / 2
    y = (height - fh) / 2
    # 逐个绘制文字
    for s in strs:
        draw.text((x, y), s, color_text_random(), font=font)
        x += fw / len(strs)

    # 模糊图片
    im = im.filter(ImageFilter.BLUR)
    im.save(r'E:\Programs\Python\python_daily\test_0011\verify_code_image.jpg', 'jpeg')
    im.show()


if __name__ == '__main__':
    draw_image(text)
