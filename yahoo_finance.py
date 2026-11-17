import yfinance as yf 

ISA = {"SGLP.L": None, "0P0000SAVS.L": None, "IE00BK5BQT80.SG": None, "0P0000KM24.L": None}
LISA = {"0P0000TK2K.L": None, "0P0000UGLE.L": None, "0P0000WGN4.L": None, "0P0000JLBQ.L": None, "0P0000KSP4.L": None, "RENG.L": None}

def getWatchList(account):

    for asset in account.keys():
        ticker = yf.Ticker(asset)
        stat = ticker.get_fast_info()
        print(asset, stat['lastPrice'], stat['regularMarketPreviousClose'])
        if stat['lastPrice'] or stat['regularMarketPreviousClose'] == 'nan':
             print('continue')
        else:
            print(stat["lastPrice"], stat["regularMarketPreviousClose"])
            percent = stat['lastPrice'] / stat['regularMarketPreviousClose'] * 100
            print(percent)
            account[asset] += ('lastPrice', 'regularMarketPreviousClose', percent,) 
        
                       
    return account

getWatchList(ISA)
#print(getWatchList(ISA))

def writeCSV():

    return

def writeTXT():
    
    return




