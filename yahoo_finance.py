import yfinance as yf 

ISA = {"SGLP.L": None, "0P0000QSAVS.L": None, "IE00BK5BQP80.SG": None, "0P0000KM24.L": None}
LISA = {"0P0000TK2K.L": None, "0P0000UGLE.L": None, "0P0000WGN4.L": None, "0P0000JLBQ.L": None, "0P0000KSP4.L": None, "RENG.L": None}

def getWatchList(account):

    for asset in account.keys():
         if 
    

    return

def writeCSV():

    return

def writeTXT():
    
    return


fund =yf.Ticker("0P0000TKZK.L")         #Reading an ETF 
lastP = fund.fast_info['lastPrice']
prevP = fund.fast_info['regularMarketPreviousClose']
difP = ((lastP - prevP) / prevP) * 100

gold =yf.Ticker("SGLP.L")               #Reading an ETC
lastGP = gold.fast_info['lastPrice']
prevGP = gold.fast_info['regularMarketPreviousClose']
difGP = ((lastGP - prevGP) / prevGP) * 100

print("For Vanguard Lifestrategy the current price is : ", lastP, " with a change of ", round(difP, 2))
print("For Invesco Gold ETC : ", lastGP, " with a change of ",  round(difGP, 2),"%") 


for stat in fund.fast_info:
       print(stat, ": ", fund.fast_info[stat]) 
else: print("_____________-")

