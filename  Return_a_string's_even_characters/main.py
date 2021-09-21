def even_chars(st):
    return list(st[1::2]) if 100 > len(st) > 1 else "invalid string"


if __name__ == '__main__':
    print(even_chars("1234567890123456"))
