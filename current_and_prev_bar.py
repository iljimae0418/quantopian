# the below algorithm compares yesterday's close (labled prev_bar) with the current price (labeled curr_bar) and 
# places an order for 20 shares if the current price is above yesterday's closing price 
def initialize(context): 
  #AAPL,MSFT and SPY 
  context.securities = [sid(24),sid(5061),sid(8554)] 
def handle_data(context,data): 
  price_history = data.history(context.securities,field = "price",bar_count=2,frequency="1d") 
  for s in context.securities: 
    prev_bar = price_history[s][-2] 
    curr_bar = price_history[s][-1] 
    if curr_bar > prev_bar: 
      order(s,20) 
