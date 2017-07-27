# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生 # 成 200
# 个激活码（或者优惠券）？

import uuid


def create_code(num=200):
    codes = []
    while True:
        code = str(uuid.uuid1()).replace('-', '')
        if not code in codes:
            codes.append(code)
        if len(codes) is num:
            break
    return codes


if __name__ == '__main__':
    create_code()
