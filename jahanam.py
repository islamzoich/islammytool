import requests

re = requests.get("https://apiz-2bba99784e02.herokuapp.com/api/ip/v1/k")

try:
    data = re.json()

    Jhenm666 = ["Basrah", "Baghdad", "Erbil", "Kirkuk"]

    Jh = data[0].get("location", "")
    jh66 = Jh.split(",")[0].strip()

    if any(Jhenm669 in jh66 for Jhenm669 in Jhenm666):
        print("\033[91m" + "IP Location:", Jh + "\nAccess granted." + "\033[0m")
    else:
        print("\033[93m" + "IP Location:", Jh + "\nAccess denied." + "\033[0m")
except Exception as e:
    print("Error:", e)
