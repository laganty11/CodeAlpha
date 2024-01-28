from alpha_vantage.timeseries import TimeSeries
import json

class PortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] <= 0:
                del self.portfolio[symbol]
        else:
            print(f"Error: {symbol} not found in the portfolio.")

    def track_performance(self):
        ts = TimeSeries(key='YOUR_ALPHA_VANTAGE_API_KEY')  # Replace with your Alpha Vantage API key

        total_value = 0
        for symbol, quantity in self.portfolio.items():
            data, meta_data = ts.get_quote_endpoint(symbol=symbol)
            if '05. price' in data:
                price_per_unit = float(data['05. price'])
                value = price_per_unit * quantity
                total_value += value
                print(f"{symbol}: {quantity} units - Current Price: ${price_per_unit:.2f} - Value: ${value:.2f}")

        print(f"Total Portfolio Value: ${total_value:.2f}")

    def display_portfolio(self):
        print("Current Portfolio:")
        for symbol, quantity in self.portfolio.items():
            print(f"{symbol}: {quantity} units")

# Example usage:
if __name__ == "__main__":
    tracker = PortfolioTracker()

    tracker.add_stock("AAPL", 5)
    tracker.add_stock("GOOGL", 2)
    tracker.add_stock("MSFT", 3)

    tracker.display_portfolio()
    tracker.track_performance()

    tracker.remove_stock("AAPL", 2)

    tracker.display_portfolio()
    tracker.track_performance()
