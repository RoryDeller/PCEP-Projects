import yfinance as yf   

fund =yf.Ticker("0P0000TKZK.L")         #Reading an ETF 
lastP = fund.fast_info['lastPrice']
prevP = fund.fast_info['previousClose']
difP = lastP - prevP

gold =yf.Ticker("SGLP.L")               #Reading an ETC
lastGP = gold.fast_info['lastPrice']
prevGP = gold.fast_info['regularMarketPreviousClose']
difGP = (lastGP - prevGP) / prevGP * 100

print("For Vanguard Lifestrategy the current price is : ", lastP, " with a change of ", round(difP, 2))
print("For Invesco Gold ETC : ", lastGP, " with a change of ",  round(difGP, 2),"%") 


#for stat in fund.fast_info:
#       print(stat, ": ", fund.fast_info[stat]) 
#else: print("_____________-")


#for stat in gold.fast_info:
#       print(stat, ": ", gold.fast_info[stat])
