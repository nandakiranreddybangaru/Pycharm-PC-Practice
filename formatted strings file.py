print('***  CURRYS PC WORLD BILL RECEIPT')
print('--> Hyderabad <--')

item = 'wirelessheadphones'
original_price = 15300.00
discount = 0.1
gst = 0.19
subtotal_price = original_price - (original_price * discount)
tax = subtotal_price * gst
total_before_shipping = subtotal_price + tax
if total_before_shipping > 1000:
    shipping_price = 0
else:
    shipping_price = 50
final_price = shipping_price + total_before_shipping

print(f'Wireless Headphones : ₹{original_price}')

print(f'After Discount :      ₹{subtotal_price}')
print(f'GST (9%) :            ₹{tax:.2f}')
print(f'Shipping charges: {shipping_price:.2f}')
print('----------*****---------')
print(f'Total Price : ₹{final_price:.3f}')



