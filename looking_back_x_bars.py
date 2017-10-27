#calculating percent change 
def initialize(context): 
  context.securities = [sid(24),sid(39840)] 
def handle_data(context,data): 
  prices = data.history(context.securities,fields = "price",bar_count = 10,frequency = "1d") 
  pct_change = (prices.ix[-1]-prices.ix[0])/prices.ix[0] 
  log.info(pct_change) 
'''' 
#Same code may be re-written as 
def initialize(context): 
  context.securities = [sid(24),sid(5061),sid(8554)] 
def handle_data(context,data): 
  price_history = data.history(context.securities,field = "price",bar_count = 10,frequency = "1d") 
  pct_change = price_history.iloc[[0,-1]].pct_change() 
  log.info(pct_change) 
''''
