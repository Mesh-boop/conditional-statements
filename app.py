def calculate_discount(price, discount_percent):
 """calculates final price after applying dicount"""
 if discount_percent >= 20:
    discount_amount = (price * discount_percent / 100)
    final_price = price - discount_amount
    return final_price
 else:
    return price  #No discount


price = float(input("Enter price:"))
discount_percent = float(input("Enter discount:"))


final_price = calculate_discount(price, discount_percent)

if discount_percent >=20:
   print(f"Discount Applied! final price is{final_price:.2f}")

else: 
   print(f"No discount applied:{final_price:.2f}")   
