# The customer's shopping cart prices
cart_prices = [450.00, 1200.50, 299.99, 3500.00, 50.00, 1050.00]

print("--- Premium Items in Cart ---")

total = 0
for prices in cart_prices:

    total = total + prices

print(f'Item Prices: {cart_prices}')
print(f"Total: ₹{total}")
# YOUR TURN: 
# 1. Write a 'for' loop to go through each price in 'cart_prices'
# 2. Inside the loop, write an 'if' statement to check if the price is greater than 1000
# 3. If it is greater than 1000, print: f"High-value item found: ₹{price}"