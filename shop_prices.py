prices = tuple(map(float, input("Enter prices: ").split(',')))
print("Total number of items sold:", len(prices))
if len(prices) > 0:
    print("Cheapest item price:", min(prices))
    max_price = max(prices)
    print("Costliest item price:", max_price)
    print("Prices in ascending order:", tuple(sorted(prices)))
    count_max = prices.count(max_price)
    print("Number of costliest items sold:", count_max)
else:
    print("No items sold")