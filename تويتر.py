#-----------------------------------------------
# ⚡ Zeus Twitter Checker — @R7_36~Zeus
#-----------------------------------------------

import webbrowser
try:
    webbrowser.open('https://t.me/R7Aih1')
except Exception:
    pass

import requests
import json
import random
import sys
from threading import Thread
import os
import time

# ==================== الألوان ====================
Z = '\x1b[1m\x1b[32m'
Y = '\x1b[1m\x1b[33m'
R = '\x1b[1m\x1b[31m'
W = '\x1b[1m\x1b[37m'
C = '\x1b[1m\x1b[36m'
X = '\x1b[0m'
P='\x1b[38;5;231m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
cyan = "\033[1m\033[36m"
x = '\x1b[1;33m'
white = '\x1b[1;37m'
z = '\x1b[1;31m'

blue_ansi = '\033[1;34m'
orange = blue_ansi 
gg = blue_ansi

E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'
G = '\033[1;34m'
HH = '\033[1;34m'
M = '\x1b[1;37m'
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
magenta = "\033[1m\033[35m"
white = "\033[1m\033[37m"
reset = "\033[0m"

a1 = '\x1b[1;31m'
a2 = '\x1b[1;34m'
a3 = '\x1b[1;32m'
a4 = '\x1b[1;33m'
a9 = '\x1b[1;37m'

aras1 = 0  
aras2 = 0  
aras3 = 0  
aras4 = 0  
is_running = True

os.system('clear' if os.name != 'nt' else 'cls')

# ==================== الشعار المتحرك ====================
LOGO_LINES = [
    "",
    "     Z E U S",
]

LOGO2_LINES = [
    "╱╱╭━━━┳━┳━━━┳━╮",
    "╭━┫╭━╮┃━┫╭━╮┃━┫",
    "┃╋┣╯╭╯┣━┣╯╭╯┣━┃",
    "┃╭╯╱┃╭┻━╯╱┃╭┻━╯",
    "╰╯╱╱┃┃╱╱╱╱┃┃",
]

CYAN = "\033[38;5;51m"

def animate_logo():
    """لوكو متحرك بلون سماوي"""
    os.system('clear' if os.name != 'nt' else 'cls')
    print()
    for line in LOGO_LINES:
        buf = ""
        for ch in line:
            buf += ch
            sys.stdout.write("\r" + CYAN + buf + reset)
            sys.stdout.flush()
            time.sleep(0.04)
        print(CYAN + buf + reset)
        time.sleep(0.05)
    print()
    for line in LOGO2_LINES:
        buf = ""
        for ch in line:
            buf += ch
            sys.stdout.write("\r" + CYAN + buf + reset)
            sys.stdout.flush()
            time.sleep(0.02)
        print(CYAN + buf + reset)
        time.sleep(0.03)
    print()

def print_custom_banner():
    animate_logo()
    print(f"{CYAN}Zeus━━━━━━━━━━━━Zeus━━━━━━ {green} @R7_36~Zeus {CYAN}━━━━━━Zeus━━━━━━{reset}")
    print(f"{CYAN}   TWITTER CHECKER — ZEUS EDITION {reset}")
    print(f"{CYAN}   Dev : {green}@R7_36{reset}")
    print(f"{CYAN}   Channel : {green}@R7Aih1{reset}")
    print(f"{CYAN}━━━━━━━━━━━━━━━━━━{reset}")

os.system('clear' if os.name != 'nt' else 'cls')
print_custom_banner()

token = input(f"{a3}token:{a4} ")
ID = int(input(f"{a3} ID :{a4} "))

duration_minutes = 1440 
duration_seconds = duration_minutes * 60

webbrowser.open('https://t.me/R7Aih1')

def W4_M4():
    output = f"""
{blue_ansi}━━━━━━ {blue_ansi}  Zeus {blue_ansi}.━━━━━━
{blue_ansi}Hits : {green}{aras1}{reset}
{blue_ansi}Bad Twitter : {red}{aras2}{reset}
{blue_ansi}Total Checked : {cyan}{aras3}{reset}
{blue_ansi}Good Email : {green}{aras4}{reset}
{white}Dev : {green}@R7_36~Zeus
{white}Channel : {green}@R7Aih1
{blue_ansi}━━━━━━ {blue_ansi}  {blue_ansi}.━━━━━━{reset}
"""
    os.system('clear' if os.name != 'nt' else 'cls')
    sys.stdout.write(output)
    sys.stdout.flush()

def aras1_check(email):
    global aras1, aras2, aras3, aras4
    try:
        time.sleep(0.3)
        headers = {
            'accept': '*/*',
            'accept-language': 'ar',
            'origin': 'https://x.com',
            'referer': 'https://x.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Gecko) Chrome/142.0.0.0 Safari/537.36',
        }
        params = {'email': email}
        response = requests.get('https://api.x.com/i/users/email_available.json', params=params, headers=headers)
        result = response.text
        
        aras3 += 1
        
        if '"taken":true' in result:
            aras1 += 1
            aras4 += 1
            W4_M4()
            ff = f'''
     Zeus جابلك حساب تويتر 
Hit : {aras1}  
 Email : {email}  
 Dev : R7Aih1@
Channel : @R7Aih1
Zeus━━━━━━━━━━━━Zeus━━━ .
            '''
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ff}")
            with open('twitter_hits.txt', 'a') as f:
                f.write(f"{email}\n")
        else:
            aras2 += 1
            W4_M4()
    except:
        aras2 += 1
        W4_M4()

def aras4_generate():
    chars = 'qwertyuiopasdfghjklzxcvbnm0123456789'
    username = ''.join(random.choice(chars) for _ in range(3))
    return username + '@yopmail.com'

def arasPr():
    global is_running
    if not is_running:
        return
    email = aras4_generate()
    aras1_check(email)

def timer_monitor(duration):
    global is_running
    time.sleep(duration)
    is_running = False
    print(f"\n{red}[!] انتهت الـ 24 ساعة المحددة للأداة. تم الإيقاف التلقائي.{reset}")
    os._exit(0)

os.system('clear' if os.name != 'nt' else 'cls')
W4_M4()

Thread(target=timer_monitor, args=(duration_seconds,), daemon=True).start()

def loop_wrapper():
    for _ in range(5000):
        if not is_running:
            break
        arasPr()

for _ in range(10):
    Thread(target=loop_wrapper).start()
   