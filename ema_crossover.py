import talib 

def initialize(context):  
    schedule_function(open_positions, date_rules.every_day(),  time_rules.market_open(minutes = 15))
    schedule_function(close_positions, date_rules.every_day(), time_rules.market_close(minutes = 11))
    
    schedule_function(record_variables, date_rules.every_day(), time_rules.market_close())
    
    context.aapl = sid(24)  
    
def open_positions(context, data):
    my_stock_series = data.history(context.aapl,fields="price",bar_count=50,frequency="1d")
    ema1_res = talib.EMA(my_stock_series,timeperiod=17) 
    ema2_res = talib.EMA(my_stock_series,timeperiod=40) 
    ema1 = ema1_res[-1]  
    ema2 = ema2_res[-1]  
    current_positions = context.portfolio.positions[context.aapl].amount  
    if (ema1 > ema2) and current_positions == 0:  
        order_target_percent(context.aapl, 4.0)

def close_positions(context, data):
    my_stock_series = data.history(context.aapl,fields="price",bar_count=50,frequency="1d")
    ema1_res = talib.EMA(my_stock_series,timeperiod=17) 
    ema2_res = talib.EMA(my_stock_series,timeperiod=40) 
    ema1 = ema1_res[-1]  
    ema2 = ema2_res[-1]  
    current_positions = context.portfolio.positions[context.aapl].amount      
    if (ema1 < ema2) and current_positions != 0:  
        order_target_percent(context.aapl, 0)  
        
def record_variables(context, data):        
    record(Cash=context.portfolio.cash)
