import random


def adjust_stock_price(stock_market, baseline_stocks):
    """Adjusts the stock price based on available stocks."""
    supply_ratio = stock_market["available_stocks"] /baseline_stocks
    stock_market["price"] = max(1.0, 100.0 * (1 / supply_ratio))  # Price inversely proportional to supply ratio
    stock_market["price"] = round(stock_market["price"], 2)

def stock_management(stock_market):
    """Randomly adjusts the stock price and recalculates available stocks."""
    adjustment_factor = random.uniform(0.5, 1.5)  # Random multiplier between 0.5 and 1.5
    stock_market["price"] *= adjustment_factor  # Adjust stock price
    stock_market["available_stocks"] = int(stock_market["available_stocks"] / adjustment_factor)  # Adjust number of stocks
    stock_market["price"] = round(stock_market["price"], 2)  # Round to 2 decimal places

def trade_stock(player, stock_market = {"price": 100.0, "available_stocks": 1000 }, buy="none"):
    """Allows a player to buy or sell stocks."""
    if buy == "buy":
        max_affordable_stocks = int(player.money / stock_market["price"])
        stocks_to_buy = random.randint(1, max_affordable_stocks) if max_affordable_stocks > 0 else 0

        if stocks_to_buy <= stock_market["available_stocks"] and stocks_to_buy > 0:
            total_cost = stocks_to_buy * stock_market["price"]
            player.money -= total_cost
            player.stocks += stocks_to_buy
            stock_market["available_stocks"] -= stocks_to_buy
            print(f"{player.id} bought {stocks_to_buy} stocks for ${total_cost:.2f}")
        else:
            print(f"{player.id} cannot afford or stocks unavailable for buying.")
    elif buy == "sell":
        stocks_to_sell = random.randint(1, player.stocks) if player.stocks > 0 else 0

        if stocks_to_sell > 0:
            total_earnings = stocks_to_sell * stock_market["price"]
            player.money += total_earnings
            player.stocks -= stocks_to_sell
            stock_market["available_stocks"] += stocks_to_sell
            print(f"{player.id} sold {stocks_to_sell} stocks for ${total_earnings:.2f}")
        else:
            print(f"{player.id} has no stocks to sell.")
    else:
        pass