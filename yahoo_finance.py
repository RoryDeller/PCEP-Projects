import yfinance as yf
from decimal import Decimal as d, ROUND_HALF_EVEN

ISA = {"SGLP.L": (), "IE00BK5BQT80.SG": (), "0P0000SAVS.L": (), "0P0000KM24.L": ()}
LISA = {"0P0000TK2K.L": (), "0P0000UGLE.L": (), "0P0000WGN4.L": (), "0P0000JLBQ.L": (), "0P0000KSP4.L": (), "RENG.L": ()}

def getWatchList(account):                  #Use .info to retrive the last market day closed price and the current market price
                                            #Decimal module allows precise rounding to the recorded market value on Stocks App
    for asset in account.keys():
        stat = yf.Ticker(asset)
        if ['regularMarketPrice'] == None or ['regularMarketPreviousClose'] == None:
            percentR = None
        else:
            current, last, state = stat.info['regularMarketPrice'], stat.info['regularMarketPreviousClose'], stat.info['marketState']
            percent = round((((current - last) / last) *  100),3)
            percentR = float(d(str(percent)).quantize(d('0.01'), rounding=ROUND_HALF_EVEN))
        account[asset] = (current, last,  percentR, state) 
                 
    return account

def writeCSV():

    return

def writeTXT(account):
    with open('watchlist.txt', 'w') as file:
        for ticker,stats in account.items():
            file.write(f"{ticker}: {stats} \n")
            #print(ticker, stats)
    
    with open('watchlist.txt', 'r') as file:
        return file.read()
    
    

watchlist = writeTXT(getWatchList(ISA))
print(watchlist)


