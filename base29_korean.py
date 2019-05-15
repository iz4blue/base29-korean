# -*- coding: utf-8 -*-

# http://www.crockford.com/wrmg/base32.html 의 base32 를 기준으로
# 한국어의 발음상 E 와 2 가 같은 것을 고려, 값이 2임
# 한국어의 발음상 5 와 O 가 같은 것을 고려, O는 0으로 취급되어 값이 0임
# 읽고 쓰기 편한 것을 목적으로 u 와 v 을 같은 문자로 취급,
# 소문자 q 와 9 가 같을 수 있는 것을 고려, 숫자 9로 치환, 그러나 숫자중 5가 없어 값음 8임
symbols = '012346789ABCDFGHJKMNPRSTVWXYZ'


def encode(number):
    if int(number) < 0:
        raise ValueError("'%d' 은 양수가 아닙니다" % number)

    value = int(number)
    if value == 0:
        return '0'

    output = ''
    while value > 0:
        char = value % len(symbols)
        value //= len(symbols)
        output = symbols[char] + output

    return output


def decode(source):
    trantab = bytearray.maketrans(b'5EeIiLlOoUuQq', b'022111100VV99')

    string = source.translate(trantab)
    string.upper()

    number = 0
    for char in string:
        number = number * len(symbols) + symbols.index(char)

    return number
