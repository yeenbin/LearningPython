#字符串
print('包含中文的str')

#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('a'))
print(ord('中'))

print(chr(97))
print(chr(25991))

#十六进制
print('\u4e2d\u6587')

#编码
print('-------------------------------------')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))


#解码
print('-------------------------------------')
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
