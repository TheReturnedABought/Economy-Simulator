import random
from Person import Person
import stocks
import stock_graph_interface

# Global variables
players = []
stock_market = {
    "price": 100.0,  # Initial price per stock
    "available_stocks": 100000  # Total stocks available in the market
}
baseline_stocks = stock_market["available_stocks"]
def start():
    """Initializes players with random starting money and zero stocks."""
    global players
    num_players = 5  # Number of players in the game
    players = [Person(id=i + 1, money=random.randint(500, 2000)) for i in range(num_players)]
    stocks.start = True

def main():
    """Main function to simulate the stock trading game."""
    start()
    global stock_market

    print("Initial state of players:")
    for player in players:
        print(player)

    for round_num in range(1, 4):  # Simulate 23 rounds of trading
        print(f"\nRound {round_num}")
        stocks.stock_management(stock_market)
        print(f"Updated stock price: ${stock_market['price']}, Available stocks: {stock_market['available_stocks']}")

        for player in players:
            if player.money >= 200:
                action = random.choice(["buy", "none","sell"])
                stocks.trade_stock(player, stock_market, buy=(action == "buy"))

        print("\nState of players after this round:")
        for player in players:
            if player.money < 200:
                print(f"{player} has less than $200, they are working...")
                player.produce_value()
            else:
                print(player)
            player.money -= 200
    stock_prices = []

    for round_num in range(1, 11):  # Simulate 10 rounds of trading
        # Other existing code...
        stock_prices.append(stock_market["price"])
        stocks.adjust_stock_price(stock_market, baseline_stocks)
    # Display the stock price trend
    stock_graph_interface.display_graph(stock_prices)

if __name__ == "__main__":
    main()