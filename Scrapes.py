# -*- coding: utf-8 -*-

from six.moves import urllib
import json
import pandas as pd

# add Coinmetrics' key and file destination
key = 'your_API_key'
dest = r'file_directory'

def getUserTransaction(coin = 'btc', op = 'transactions', size = '1000'):   
    # expect string inputs. View Coinmetrics API documentation for more.
    # make sure key works   
    
    # get records with given uid and txnType
    url = 'https://api.coinmetrics.io/v4/blockchain/' + coin \
        + '/' + op + key + '&page_size=' + size
        
    # get data
    response = urllib.request.urlopen(url)
    data = json.load(response)["data"]
    
    # save as csv
    pd.read_json(json.dumps(data)).to_csv(dest + coin + op + '.csv', index = None)
