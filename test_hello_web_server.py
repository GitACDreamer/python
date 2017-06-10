from wsgiref.simple_server import make_server
from test_hello_web import application

if __name__ == '__main__':
    # 创建一个服务器
    httpd = make_server('', 8000, application)
    print('Serving Http on port 8000……')
    # 开始监听
    httpd.serve_forever()
