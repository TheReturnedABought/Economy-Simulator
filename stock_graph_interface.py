import matplotlib.pyplot as plt

def display_graph(stock_prices):
    """Displays a graph of stock price trends over time."""
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(stock_prices) + 1), stock_prices, marker='o', label='Stock Price')
    plt.title('Stock Price Trend Over Time')
    plt.xlabel('Rounds')
    plt.ylabel('Price ($)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Example usage of the graph interface
    sample_prices = [100.0, 120.0, 110.0, 150.0, 140.0, 160.0, 170.0, 165.0, 175.0, 180.0]
    display_graph(sample_prices)