#Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a formatted output one currency at a time.
#The output should display the name of the currency, the symbol (if applicable), the current price and % change in the last 24 hrs and corresponding price (based on % change)
#Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC and $3,000 for ETH.
#Submit your GitHub URL which should contain all the files worked in class as well as the above.
from distutils.util import change_root
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client

accountSID = 'private'

authToken = 'private'

client = Client(accountSID,authToken) #authenticates us prior to sending message

TwilioNumber = '+private'

mycellphone = 'private'


url = 'https://8marketcap.com/cryptos/'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

title = soup.title

#print(title.text)

table_rows = soup.findAll('tr')

for x in range(1, 6):
    td = table_rows[x].findAll("td")
    name = td[2].text.strip('\n')
    symbol= td[3].text.strip('\n')  
    current_price = td[5].text.strip('\n')  
    percent_change = td[6].text.strip('\n')
    price = float(td[5].text.replace(",", "").replace("$", ""))
    change = float(td[6].text.strip('%'))/100
    change_in_price = round(price - (price * change),2)
    cip = "{:,}".format(change_in_price)

    print(f"Company Name: {name}")
    print(f"Current Price: {current_price}")
    print(f"24hr % change: {percent_change}")
    print(f"Starting Price: ${cip}")
    input()

    if name == 'Bitcoin' and price < 40000:
        textmessage = client.messages.create(to= mycellphone, from_= TwilioNumber, body = 'Invest in BTC')
    if name == 'Ethereum' and price < 3000:
        textmessage = client.messages.create(to= mycellphone, from_= TwilioNumber, body = 'Invest in Ethereum')



