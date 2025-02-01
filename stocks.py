import random

def adjust_stock_price(stock_market, baseline_stocks):
    supply_ratio = stock_market["available_stocks"] / baseline_stocks
    stock_market["price"] = max(1.0, 100.0 * (1 / supply_ratio))
    stock_market["price"] = round(stock_market["price"], 2)

def stock_management(stock_market):
    adjustment_factor = random.uniform(0.5, 1.5)
    stock_market["price"] *= adjustment_factor
    stock_market["available_stocks"] = int(stock_market["available_stocks"] / adjustment_factor)
    stock_market["price"] = round(stock_market["price"], 2)

def trade_stock(player, stock_market=None, buy="none"):
    if stock_market is None:
        stock_market = {"price": 100.0, "available_stocks": 1000}  # Fix: Avoid mutable default
    if buy == "buy":
        max_affordable_stocks = int(player.money / stock_market["price"])
        stocks_to_buy = random.randint(1, max_affordable_stocks) if max_affordable_stocks > 0 else 0
        if stocks_to_buy > 0 and stocks_to_buy <= stock_market["available_stocks"]:
            total_cost = stocks_to_buy * stock_market["price"]
            player.money -= total_cost
            player.stocks += stocks_to_buy
            stock_market["available_stocks"] -= stocks_to_buy
            print(f"Player {player.id} bought {stocks_to_buy} stocks for ${total_cost:.2f}")
        else:
            print(f"Player {player.id} cannot buy stocks.")
    elif buy == "sell":
        stocks_to_sell = random.randint(1, player.stocks) if player.stocks > 0 else 0
        if stocks_to_sell > 0:
            total_earnings = stocks_to_sell * stock_market["price"]
            player.money += total_earnings
            player.stocks -= stocks_to_sell
            stock_market["available_stocks"] += stocks_to_sell
            print(f"Player {player.id} sold {stocks_to_sell} stocks for ${total_earnings:.2f}")
        else:
            print(f"Player {player.id} has no stocks to sell.")
