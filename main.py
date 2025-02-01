import random
from Person import Person
import stocks
import stock_graph_interface

players = []
stock_market = {
    "price": 100.0,
    "available_stocks": 100000
}
baseline_stocks = stock_market["available_stocks"]


def start():
    global players
    num_players = 5
    players = [Person(id=i + 1, money=random.randint(500, 2000)) for i in range(num_players)]


def main():
    start()
    stock_prices = []

    print("Initial state of players:")
    for player in players:
        print(player)

    total_rounds = 10  # Simulate 10 rounds
    for round_num in range(1, total_rounds + 1):
        print(f"\n--- Round {round_num} ---")

        # Random stock adjustment
        stocks.stock_management(stock_market)
        print(
            f"Random Adjustment: Price=${stock_market['price']:.2f}, Stocks Available: {stock_market['available_stocks']}")

        # Players trade
        for player in players:
            if player.money >= 200:
                action = random.choice(["buy", "none", "sell"])
                stocks.trade_stock(player, stock_market, buy=(action == "buy"))
            else:
                print(f"Player {player.id} is working to earn money.")
                player.produce_value()

        # Supply-based price adjustment
        stocks.adjust_stock_price(stock_market, baseline_stocks)
        stock_prices.append(stock_market["price"])
        print(
            f"Supply Adjustment: New Price=${stock_market['price']:.2f}, Stocks Available: {stock_market['available_stocks']}")

        # Deduct $200 from all players
        print("\nPlayers' status after deductions:")
        for player in players:
            player.money = max(0, player.money - 200)  # Prevent negative money
            print(player)

    # Display the stock price graph
    stock_graph_interface.display_graph(stock_prices)


if __name__ == "__main__":
    main()
