import random
import requests
from datetime import datetime



Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
B = '\033[2;36m'
Y = '\033[1;34m'
r="\033[1;31m"
print(r +'' '''  

يوزࢪات تلي                  
''' '')

md = 0
ID = input(f'{Y}ID {C}={X}={Z}={F}>{B} ')

print(f'{Z}={X}={Z1}={F}={A}={C}={B}={Y}={Z}={X}={Z1}={F}={A}={C}={B}={Y}={Z}={X}={Z1}={F}={A}={C}={B}={Y}=')

tok = input(f'{Y}TOKEN {B}={Z}={C}>{B}  ')

print(f'{Z}={X}={Z1}={F}={A}={C}={B}={Y}={Z}={X}={Z1}={F}={A}={C}={B}={Y}={Z}={X}={Z1}={F}={A}={C}={B}={Y}=')

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
abc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

v1 = ''.join(random.choice(abc1) for i in range(1))
v2 = ''.join(random.choice(abc) for i in range(1))
v3 = ''.join(random.choice(abc) for i in range(1))
v4 = ''.join(random.choice(abc) for i in range(1))
user_list = []

for _ in range(1000):  # يمكنك تغيير الرقم إلى عدد المرات التي تريد أن يفحص فيها
    v1 = ''.join(random.choice(abc1) for i in range(1))
    v2 = ''.join(random.choice(abc) for i in range(1))
    v3 = ''.join(random.choice(abc) for i in range(1))

    user = v1 + v4 + v2 + '_' + v3
    user2 = v2 + v4 + '_' + v1 + v3
    user3 = v1 + v2 + '_' + v3 + v4
    hamo010 = (user, user2, user3)
    user = random.choice(hamo010)
    url = requests.get(f'https://t.me/{user}').text
    if 'tgme_username_link' in url:
        md += 1
        requests.get(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=ʜɪ ᴘʀᴏ ᴘᴀᴛʀᴇᴋ ɴᴇᴡ ᴜᴤᴇʀ\n‌=‌=‌=‌‌=‌=‌‌=‌=‌‌=‌=‌‌=‌=‌‌=‌=‌=‌\n𝑈𝑆𝐸𝑅 ➪ @{user}\n‌=‌=‌=‌‌=‌=‌‌=‌=‌‌=‌=‌‌=‌=‌‌=‌=‌=‌\n')
        print(f'{C}[{md}]{F}DonE UseR : ' + user)
        user_list.append(user)
    else:
        md += 1
        print(f'{X}[{md}]{Z}ErrOR UseR : ' + user)


#صيد يوزرات تلي
