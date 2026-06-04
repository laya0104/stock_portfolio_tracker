stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 170
}

portfolio = {}
total_investment = 0

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input("Enter stock symbol (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        print("Stock not available!")

print("\nPortfolio Summary")
print("-" * 30)

for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${investment}")

print("-" * 30)
print(f"Total Investment Value: ${total_investment}")

with open("portfolio_summary.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-" * 30 + "\n")

    for stock, qty in portfolio.items():
        investment = stock_prices[stock] * qty
        file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${investment}\n")

    file.write("-" * 30 + "\n")
    file.write(f"Total Investment Value: ${total_investment}")

print("\nPortfolio saved to 'portfolio_summary.txt'")