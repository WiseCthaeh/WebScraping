# -*- coding: utf-8 -*-

from six.moves import urllib
import json
import pandas as pd

def getUserTransaction(coin = 'btc', op = 'transactions', size = '1000'):   
    # expect string inputs. View Coinmetrics API documentation for more.
    # make sure key works   
    
    # get records with given uid and txnType
    url = 'https://api.coinmetrics.io/v4/blockchain/' + coin \
        + '/' + op + '?api_key=I9e8A25wKUtV6fNnhkpk&page_size=' + size
        
    # get data
    response = urllib.request.urlopen(url)
    data = json.load(response)["data"]
    
    # save as csv
    pd.read_json(json.dumps(data)).to_csv(r'C:\\Users\\marco\\OneDrive - Imperial College London\\Trabajo\\Ethereum\\Tokens\\Coinmetrics\\' \
              + coin + op + '.csv', index = None)
        
getUserTransaction('zrx')
getUserTransaction('zrx', 'accounts')
getUserTransaction('zrx', 'balance-updates')
getUserTransaction('zrx', 'blocks')