'contextlib 的使用'

from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen


class Query(object):
    def __init__(self, name):
        self._name = name

    def query(self):
        print('Query info about %s...' % self._name)


@contextmanager
def create_query(name):
    print('Begin...')
    q = Query(name)
    yield q
    print('End...')


@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

def testContextlib():
    with create_query('Bob') as q:
        q.query()

    with tag('h1'):
        print('hello')
        print('world')

    with closing(urlopen('https://www.python.org')) as page:
        for line in page:
            print(line)


if __name__ == '__main__':
    testContextlib()
