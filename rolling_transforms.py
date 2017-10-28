#moving average 
def initialize(context): 
  context.securities = [sid(24),sid(5061),sid(8554)] 
def handle_data(context,data): 
  price_history = data.history(context.securities,fields = "price",bar_count =5,frequency = "1d") 
  log.info(price_history.mean()) 
