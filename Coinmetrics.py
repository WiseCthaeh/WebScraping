# -*- coding: utf-8 -*-

from six.moves import urllib
import json
import pandas as pd

# key needed for quick scrapes
your_key = 'your_Coinmetrics_key'

# use two // instead of one to avoid bugs
dest = 'your_file_directory'

def getUserTransaction(coin = 'eth', op = 'transactions', size = '10000'):   
    # expect string inputs. View Coinmetrics API documentation for more.
    
    # get records with given uid and txnType (coin)
    url = 'https://api.coinmetrics.io/v4/blockchain/' + coin \
        + '/' + op + your_key + size

    # get data
    response = urllib.request.urlopen(url)
    data = json.load(response)["data"]
    
    # save as csv
    pd.read_json(json.dumps(data)).to_csv(dest + coin + '_' + op + '.csv', index = None)

# list of tokens to scrape
tokens = ['eth', 'zrx', 'mkr', 'pax', 'snx']

# list of 'forbidden' tokens in Coinmetrics as of Jan 2022
forbidden = [
    'rep', 'bnt', 'bat', 'cennz', 'cnd', 'cvc', 'cro', 'dai', 'mana', 'drgn',
    'eng', 'ftt', 'fun', 'gas', 'gusd', 'gno', 'gnt', 'hedg', 'ht', 'kcs', 
    'knc', 'loom', 'lrc', 'maid', 'mco', 'neo', 'mxm', 'okb', 'omg', 'poly',
    'ppt', 'powr', 'qash', 'qnt', 'ren', 'salt', 'sai', 'srn', 'snt', 'storj', 
    'veri', 'wtc', 
    ]

# list of Eth tokens not tracked by Coinmetrics as of Jan 2022
not_tokens = [
    'aac', 'adx', 'alf', 'abt', 'atm', 'bix', 'bcv', 'btmx', 'bix', 'bcv',
    'btmx', 'btt', 'bczero', 'chz', 'cloak', 'ccc', 'cob', 'crpt', 'data', 
    'dbc', 'dcn', 'dent', 'dgtx', 'dgd', 'drg', 'drop', 'dx', 'edg', 'ekt',
    'egt', 'enj', 'xet', 'xuc', 'ftm', 'fet', 'game', 'gto', 'hbar', 'hot',
    'rlc', 'inb', 'jct', 'lamb', 'lky', 'mati', 'mtl', 'min', 'mith', 'xin',
    'mgo', 'mof', 'nex', 'bat', 'nexo', 'noah', 'ncash', 'ode', 'orbs', 'plr',
    'poe', 'npxs', 'liquid', 'qsp', 'qbit', 'rdn', 'repo', 'req', 'rev',
    'rift', 'san', 'seele', 'slv', 'sngls', 'solve', 'eurs', 'sub', 'sxp',
    'pay', 'usdt', 'thr', 'topc', 'tusd', 'uuu', 'leo', 'usc', 'vest', 'vibe',
    'win', 'xmx', 'zb'
    ]

if __name__== '__main__':
    
    for token in tokens:        
        print(token)
        getUserTransaction(coin = token)
        getUserTransaction(coin = token, op = 'accounts')
        getUserTransaction(coin = token, op =  'balance-updates')
        getUserTransaction(coin = token, op = 'blocks')       
