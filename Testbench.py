import requests
url = "https://www.tcgplayer.com/product/225211/flesh-and-blood-tcg-welcome-to-rathe-fyendals-spring-tunic?page=1&Language=English&Printing=Unlimited+Edition+Rainbow+Foil"
page = requests.get(url)

print(page.text)