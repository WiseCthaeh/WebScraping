# -*- coding: utf-8 -*-

from six.moves import urllib
import json
import pandas as pd

def getUserTransaction(coin = 'eth', op = 'transactions', size = '10000'):   
    # expect string inputs. View Coinmetrics API documentation for more.
    # make sure key works   
    
    # get records with given uid and txnType
    url = 'https://api.coinmetrics.io/v4/blockchain/' + coin \
        + '/' + op + '?api_key=I9e8A25wKUtV6fNnhkpk&page_size=' + size

    # get data
    response = urllib.request.urlopen(url)
    data = json.load(response)["data"]
    
    # save as csv
    pd.read_json(json.dumps(data)).to_csv(
        r'C:\\Users\\marco\\OneDrive - Imperial College London\\Trabajo\\Ethereum\\Tokens\\Coinmetrics\\' \
              + coin + '_' + op + '.csv', index = None)

tokens = ['eth', 'zrx', 'mkr', 'pax', 'snx']

if __name__== '__main__':
    
    for token in tokens:
        
        print(token)
        getUserTransaction(coin = token)
        getUserTransaction(coin = token, op = 'accounts')
        getUserTransaction(coin = token, op =  'balance-updates')
        getUserTransaction(coin = token, op = 'blocks')       
        
#%%

tokens_old = ['zrx', 'aac', 'adx', 'alf', 'alf', 'abt', 'atm', 'rep', 'bnt', 'bat',
          'bat', 'bix', 'bcv', 'btmx', 'btt', 'bczero', 'cennz', 'chz', 'cnd',
          'cvc', 'cloak', 'ccc', 'cob', 'crpt', 'cro', 'dai', 'data', 'mana', 
          'dbc', 'dcn', 'dent', 'dgtx', 'dgd', 'drgn', 'drg', 'drop', 'dx', 
          'edg', 'ekt', 'egt', 'eng', 'enj', 'xet', 'xuc', 'ftm', 'fet', 'ftt',
          'fun', 'game', 'gas', 'gusd', 'gto', 'gno', 'gnt', 'hbar', 'hedg', 
          'hot', 'ht', 'rlc', 'inb', 'jct', 'kcs', 'knc', 'lamb', 'lky',
          'loom', 'lrc', 'maid', 'mkr', 'mati', 'mxm', 'mco', 'mtl', 'min',
          'mith', 'xin', 'mgo', 'mof', 'nex', 'neo', 'nexo', 'noah', 'ncash',
          'ode', 'okb', 'omg', 'orbs', 'pax', 'plr', 'poe', 'poly', 'ppt', 
          'powr', 'npxs', 'qash', 'liquid', 'qnt', 'qsp', 'qbit', 'rdn', 'ren',
          'repo', 'req', 'rev', 'rift', 'salt', 'san', 'seele', 'slv', 'sai',
          'sngls', 'srn', 'solve', 'eurs', 'snt', 'storj', 'sub', 'sxp', 'snx',
          'pay', 'usdt', 'thr', 'topc', 'tusd', 'uuu', 'leo', 'usc', 'veri',
          'vest', 'vibe', 'wtc', 'win', 'xmx', 'zb']

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

forbidden = [
    'rep', 'bnt', 'bat', 'cennz', 'cnd', 'cvc', 'cro', 'dai', 'mana', 'drgn',
    'eng', 'ftt', 'fun', 'gas', 'gusd', 'gno', 'gnt', 'hedg', 'ht', 'kcs', 
    'knc', 'loom', 'lrc', 'maid', 'mco', 'neo', 'mxm', 'okb', 'omg', 'poly',
    'ppt', 'powr', 'qash', 'qnt', 'ren', 'salt', 'sai', 'srn', 'snt', 'storj', 
    'veri', 'wtc', 
    ]