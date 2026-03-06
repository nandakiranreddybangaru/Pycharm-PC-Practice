products = ["Keyboard", "Mouse", "Laptop"]
prices = [200, 500, 7000]

gst_rate = 0.18
base_price = prices[0:2]
def total_price(base_price):
    tax_amount = base_price * gst_rate
    total_price = tax_amount + base_price

    print( total_price)

print('Welcome! to our new Store')
total_price(prices[0])
total_price(prices[1])
total_price(prices[2])
print("Visit again!")