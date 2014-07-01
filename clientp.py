# download stock quotes in CSV


import requests
import time

i = 0
stock_list = ['GOOG', 'YHOO', 'AOL', 'BTCUSD=X']

while (i < 10):
    base_url = 'http://download.finance.yahoo.com/d/quotes.csv'

    # retrieve data from the web server
    for stock in stock_list:
        data = requests.get(base_url,
                            params={'s': stock, 'f': 'sl1d1t1c1ohgv',
                                    'e': '.csv'})

        # write the data to csv
        with open('stocks.csv', 'a') as code:
            code.write(data.content)
        i+=1
    
    # pause for 3 secs
    time.sleep(3)