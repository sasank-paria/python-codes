import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/asus-tuf-gaming-a17-ryzen-7-octa-core-4800h-16-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-rtx-3050-fa706ic-hx003t-laptop/p/itmccc79bbd17e07?pid=COMG8N5PFPCX9Z3J&lid=LSTCOMG8N5PFPCX9Z3JGKCEFC&marketplace=FLIPKART&store=6bo%2Fb5g&srno=b_1_1&otracker=hp_reco_Laptops%2BFor%2BYou_4_10.dealCard.OMU_cid%3AS_F_NWF_PC78b008476d07b2_b___NONE_ALL%3Bnid%3A6bo_b5g_%3Bet%3APC%3Beid%3APC78b008476d07b2%3Bmp%3AF%3Bct%3Ab%3B_5&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2FintentPivoted_Laptops%2BFor%2BYou_DESKTOP_HORIZONTAL_dealCard_cc_4_NA_view-all_5&fm=personalisedRecommendation%2FintentPivoted&iid=f7d4bd1b-b8a8-4551-b5cb-3033ccd671cc.COMG8N5PFPCX9Z3J.SEARCH&ppt=hp&ppn=homepage&ssid=0np0e723ao0000001648291278079"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,hi;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(class_="_30jeq3 _16Jk6d").get_text()

# price_without_currency = price.split("$")[1]
# price_as_float = float(price_without_currency)
# print(price_as_float)

print(price)