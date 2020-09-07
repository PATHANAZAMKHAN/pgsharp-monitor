import time

def check_license_window_status():
    import requests
    from bs4 import BeautifulSoup
    r = requests.get("https://manage.pgsharp.com/cart.php")
    soup = BeautifulSoup(r.content,'html.parser')
    price_div = soup.select(".price-area")

    text = (price_div[1].a.text.rstrip().lstrip())

    if text == "Order Now":
        window_status = "Open"

    else:
        window_status = "Close"
    
    return window_status

while True:
    status = check_license_window_status()
    print(f'{time.strftime("%a,%d %B %Y %I:%M %p")}: {status}')
    time.sleep(1*60)
