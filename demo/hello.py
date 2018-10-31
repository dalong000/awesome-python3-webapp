def application(environ, start_response):
    start_reponse('200 OK', [('Content_Type', 'text/html')])
    return [b'<h1>Hello ,web!</h1>']

'''
environ:一个包含所有HTTP请求信息的dict对象
start_response:一个发送HTTP响应的函数
'''

