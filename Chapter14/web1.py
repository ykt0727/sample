from urllib.request import urlopen
with urlopen('http://higpen.jellybean.jp/') as file:
    for line in file:
        print(str(line, encoding='utf-8'), end='')