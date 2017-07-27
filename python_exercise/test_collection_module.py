'collections 模块的使用'

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


# FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key
class LastUpdateOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderedDict, self).__init__()
        # 设置容量
        self._capacity = capacity

    def __setitem__(self, key, value):
        # 检查dict里是否已经存在要增加的(key,value)中的key
        containKey = 1 if key in self else 0
        # 如果dict容量已满
        if len(self) - containKey >= self._capacity:
            # 则删除最先添加的key
            last = self.popitem(last=False)
            print('remove...', last)
        # 如果dict中已有要添加的key
        if containKey:
            # 删除原来的key
            del self[key]
            print('set...', (key, value))
        else:  # 如果dict中没有要添加的key
            print('add', (key, value))
         # 将(key,value)加入dict
        OrderedDict.__setitem__(self, key, value)


def testCollection():

    # namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    p = Point(2, 4)
    c = Circle(2, 2, 2)
    print('p.x = %d , p.y = %d' % (p.x, p.y))
    print('c.x = %d , c.y = %d , c.r = %d' % (c.x, c.y, c.r))
    print(isinstance(p, Point))
    print(isinstance(p, tuple))

    # deque
    q = deque(['a', 'b', 'c', 'd'])
    q.append('e')
    q.appendleft('i')
    e = q.pop()
    i = q.popleft()
    print(q)
    print(e)
    print(i)

    # defaultdict
    dd = defaultdict(lambda: 'N/A')
    dd['key1'] = 'abc'
    print(dd['key1'])
    print(dd['key2'])

    # OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
    d = dict([('a', 1), ('d', 4), ('b', 2), ('c', 3)])
    print(d)
    d = OrderedDict([('a', 1), ('d', 4), ('b', 2), ('c', 3)])
    print(d)

    # LastUpdateOrderedDict
    FIFO = LastUpdateOrderedDict(3)
    FIFO['a'] = 1
    FIFO['b'] = 2
    FIFO['c'] = 3
    FIFO['d'] = 4
    print(FIFO)

    # Counter
    c = Counter()
    for ch in 'programming language':
        c[ch] += 1
    print(c)


if __name__ == '__main__':
    testCollection()
