#Function to calculate the final price after applying a discount

def calculate_discount(price, discount_percentage):
    if discount_percentage >=20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
##Prompt the user for input##

original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))
if discount_percentage >= 20:
    print("Discount applied")


final_price = calculate_discount(original_price, discount_percentage)
if final_price == original_price:
    print("No discount applied. The original price is: ${:.2f}".format(original_price))
else:
    print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")