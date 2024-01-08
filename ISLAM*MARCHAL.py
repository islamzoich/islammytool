import os, sys, time, base64, marshal, zlib, py_compile

R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[1;34m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '\n\n'
banner = '\n\x1b[92m[ 1 ]\x1b[1;31m Encrypt\x1b[90m Marshal\x1b[1;31m,\x1b[1;30mZlib\x1b[1;31m,\x1b[1;30mBase64.b85\n'

os.system('clear')
print(logo)
slowprint(banner)
mainmenu = input(G + ' الـبـاسـورد > ' + C + ' > ' + Y)

if mainmenu == '1':
    os.system('clear')
    print('')
    slowprint(G + ' Launching Encryption Tool...')
    time.sleep(2)
    print('')
    file = input(G + ' اسـم الـمـلـف' + C + ' > ' + Y)
    print('')
    c = input(G + ' Output File Name' + C + ' > ' + Y)
    print('')
    slowprint(G + ' Encrypting...')
    print('')
    fileopen = open(file).read()
    sa = compile(fileopen, 'dg', 'exec')
    sb = marshal.dumps(sa)
    sc = zlib.compress(sb)
    sd = base64.b85encode(sc)
    b = '#https://t.me/RD_P0\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'
    d = open(c, 'w')
    d.write(b)
    d.close()
    time.sleep(3)
    slowprint(G + ' Encryption Completed...')
    time.sleep(3)
    print('')
    print(G + ' Output File Name: ' + Y, c)
    print('')
    print(W)
else:
    print('\x1b[91m  wrong password')
