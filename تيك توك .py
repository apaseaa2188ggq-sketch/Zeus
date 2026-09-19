# ═══════════════════════════════════════════════════════════════
#                    🎯 TIKTOK CHECKER 🎯
#                      @R7_36 ~ Zeus
# ═══════════════════════════════════════════════════════════════
import os, requests, json, time, re, random, sys, uuid, string
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from threading import Thread, Lock

# ═══ COLORS ═══
RED    = "\033[1;31m"
WHITE  = "\033[1;37m"
PINK   = "\033[1;35m"
GREEN  = "\033[1;32m"
YELLOW = "\033[1;33m"
RESET  = "\033[0m"

# ═══ ANIMATED RED LOGO ═══
KOREAN_LOGO_LINES = [
    "ㅂㅈ둎ㄴ묘ㅑㅏㅍㅌㄷㄴ퍼ㅑㅕㅐ멋넛냣아ㅛ아요ㅏㅛ",
    "아ㅛ잏틒ㅋㄹ닛뎌내ㅛㅑㅅ냣내ㅛㅇ",
    "ㄷ벼냣냣냣낳타핰효오로러처러ㅕ려려려러ㅓ퍼처러",
    "추하허ㅗ러러ㅓ처류",
    "ㅛㄱㅈㄴ포ㅑㅅㅈㅂ뎌ㅐㅐㅏㅠㅌㄴㅈ",
]

def show_animated_logo():
    os.system("cls" if os.name == "nt" else "clear")
    print()
    for line in KOREAN_LOGO_LINES:
        buf = ""
        for ch in line:
            buf += ch
            sys.stdout.write("\r" + RED + buf + RESET)
            sys.stdout.flush()
            time.sleep(0.006)
        print(RED + buf + RESET)
        time.sleep(0.06)
    print()
    time.sleep(0.3)

show_animated_logo()

# ═══ LOGIN LOGO ═══
os.system("cls" if os.name == "nt" else "clear")
logo = f"""
{PINK}●─────━Zeus─────━●
{RED}╱╱╭━━━┳━┳━━━┳━╮
{PINK}╭━┫╭━╮┃━┫╭━╮┃━┫
{RED}┃╋┣╯╭╯┣━┣╯╭╯┣━┃
{PINK}┃╭╯╱┃╭┻━╯╱┃╭┻━╯
{RED}╰╯╱╱┃┃╱╱╱╱┃┃{RESET}

{WHITE}  ×─> {WHITE}━━━━━━━{PINK}━━━━━━━━━━{WHITE}━━━━━━━━━━━━{WHITE}━━━━━{PINK}Zeus━━━━━━{WHITE}━━━━━ <─×{RESET}"""
print(logo)
print()

# ═══ INPUTS ═══
print(PINK + "  TOKEN   ➤  " + RESET, end="")
tok = input().strip()

print(PINK + "  CHAT ID ➤  " + RESET, end="")
iD = input().strip()
print()

# ═══ GLOBALS ═══
good_hot, bad_hot, good_ig, bad_ig, check = 0, 0, 0, 0, 0
ids = []
LOCK = Lock()

# ═══ PROXIES ═══
PROXIES = []

def get_proxy():
    if not PROXIES:
        return None
    p = random.choice(PROXIES)
    if not p.startswith("http"):
        p = "http://" + p
    return {"http": p, "https": p}


# ═══ RANDOM STRING ═══
def rstr(n=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(n))


# ═══ GENERATE RANDOM GMAIL-ISH USERNAME ═══
def gen_username():
    return rstr(random.randint(8, 14), string.ascii_lowercase + string.digits + "._")


# ═══ DATE FROM ID ═══
def date_sc(Id):
    try:
        i = int(Id)
        if i < 1279000: return 2010
        if i < 17750000: return 2011
        if i < 279760000: return 2012
        if i < 900990000: return 2013
        if i < 1629010000: return 2014
        if i < 2500000000: return 2015
        if i < 3713668786: return 2016
        if i < 5699785217: return 2017
        if i < 8507940634: return 2018
        if i < 21254029834: return 2019
        return "2020-2023"
    except Exception as e:
        return str(e)


# ═══ CHECK EMAIL (Instagram + Hotmail) ═══
def check_email(username):
    global good_ig, bad_ig, good_hot, bad_hot, check
    email = username + "@gmail.com"
    try:
        # فحص Instagram - هل الإيميل مستخدم؟
        rnd = str(random.randint(150, 999))
        ua = f"Instagram 311.0.0.32.118 Android (29/10; 420dpi; 1080x2129; samsung; SM-T{rnd}; qcom; en_US; 545986{rnd})"
        r = requests.post(
            "https://www.instagram.com/api/v1/web/accounts/check_email/",
            headers={"user-agent": ua},
            data={"email": email},
            proxies=get_proxy(),
            timeout=8
        )
        if "email_is_taken" in r.text:
            with LOCK: good_ig += 1
            check_hot(username)
        else:
            with LOCK: bad_ig += 1
    except Exception:
        pass

    with LOCK:
        check += 1
    sys.stdout.write(
        f"\r  {PINK}[Zeus]{RESET} Hits:{GREEN}{good_hot}{RESET} Wrong:{RED}{bad_ig}{RESET} "
        f"Good:{YELLOW}{good_ig}{RESET} Checked:{WHITE}{check}{RESET}   "
    )
    sys.stdout.flush()


# ═══ HOTMAIL CHECK ═══
def check_hot(username):
    global good_hot, bad_hot
    email = username + "@gmail.com"
    try:
        ua = "Mozilla/5.0 (iPad; CPU OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1.15"
        r = requests.post(
            "https://signup.live.com",
            headers={"user-agent": ua},
            proxies=get_proxy(),
            timeout=8
        )
        amsc = r.cookies.get_dict().get("amsc", "")
        m = re.search(r'"apiCanary":"(.*?)"', r.text)
        canary = m.group(1).encode().decode("unicode_escape") if m else ""
        if not amsc:
            return
        headers = {
            "authority": "signup.live.com",
            "canary": canary,
            "user-agent": "Mozilla/5.0 (Linux; Android 10; K) Chrome/122.0.0.0 Mobile Safari/537.36",
        }
        r2 = requests.post(
            "https://signup.live.com/API/CheckAvailableSigninNames",
            cookies={"amsc": amsc},
            headers=headers,
            json={"signInName": email},
            proxies=get_proxy(),
            timeout=8
        )
        if "isAvailable" in r2.text:
            with LOCK: good_hot += 1
            hunting(username)
        else:
            with LOCK: bad_hot += 1
    except Exception:
        pass


# ═══ HUNTING (SEND HIT) ═══
def hunting(username):
    email = username + "@gmail.com"
    try:
        # جيب معلومات انستغرام
        info = requests.get(
            f"https://anonyig.com/api/ig/userInfoByUsername/{username}",
            proxies=get_proxy(),
            timeout=8
        ).json()
        u = info.get("result", {}).get("user", {}) or {}
        Id = u.get("pk_id", "N/A")
        followers = u.get("follower_count", "N/A")
        following = u.get("following_count", "N/A")
        post = u.get("media_count", "N/A")
        name = u.get("full_name", "N/A")
        date = date_sc(Id) if Id != "N/A" else "N/A"

        hunt = (
            "              ✦ Zeus TikTok HTS ✅ ✦              \n"
            "═══════ ❖ ═════════════════\n"
            f"❖ GMAIL      ➜ {email}\n"
            f"❖ الاسم      ➜ {name}\n"
            f"❖ المعرف     ➜ {Id}\n"
            f"❖ المتابعين  ➜ {followers}\n"
            f"❖ Following  ➜ {following}\n"
            f"❖ المنشورات  ➜ {post}\n"
            f"❖ السنة      ➜ {date}\n"
            "═══════ ❖ ════════════\n"
            "❖ القناة    ➜ @R7Aih1\n"
            "❖ المطور    ➜ @R7_36\n"
            "═══════ ❖ ══════════"
        )
        requests.post(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            json={"chat_id": iD, "text": hunt},
            proxies=get_proxy(),
            timeout=8
        )
        print(PINK + "\n  [HIT] " + GREEN + email + RESET)
    except Exception:
        pass


# ═══ USERNAME WORKER ═══
def worker():
    while True:
        try:
            username = gen_username()
            check_email(username)
        except Exception:
            time.sleep(0.3)
            continue


# ═══ START THREADS ═══
print(PINK + "  [+] Starting 50 threads..." + RESET)
print(PINK + "  [+] Scanning..." + RESET)
print()

THREADS = 50
for _ in range(THREADS):
    t = Thread(target=worker, daemon=True)
    t.start()

# ═══ KEEP ALIVE ═══
try:
    while True:
        time.sleep(2)
        with LOCK:
            sys.stdout.write(
                f"\r  {PINK}[Zeus]{RESET} Hits:{GREEN}{good_hot}{RESET} "
                f"Wrong:{RED}{bad_ig}{RESET} Good:{YELLOW}{good_ig}{RESET} "
                f"Checked:{WHITE}{check}{RESET}   "
            )
            sys.stdout.flush()
except KeyboardInterrupt:
    print("\n\n" + PINK + "  Stopped by user" + RESET)
    sys.exit(0)