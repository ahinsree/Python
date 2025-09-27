# Product variables
product_name = "Laptop"
product_price = 999.99
quantity = 2
tax_rate = 0.08
in_stock = True

# Calculations
subtotal = product_price * quantity
tax_amount = subtotal * tax_rate
total_price = subtotal + tax_amount

# Display receipt
print(f"Product: {product_name}")
print(f"Price per unit: ${product_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax ({tax_rate*100}%): ${tax_amount:.2f}")
print(f"Total: ${total_price:.2f}")
print(f"In stock: {in_stock}")