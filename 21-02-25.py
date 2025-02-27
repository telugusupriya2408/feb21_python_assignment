#project _name=shopping_discount_calculator:
'''features:
Discount Calculation: Based on purchase amount, customers get discounts of 20%, 10%, or none.
Conditional Feedback: Different messages based on the discount applied.
Interactive Updates: Allows customers to add more items and recalculates the total and discount.
User-Friendly Output: Displays summaries in a clean, readable format.'''  
print("Welcome to the Shopping Discount Calculator!")

# Step 1: Input customer's name
name = input("Enter your name: ")

# Step 2: Input total purchase amount
purchase_amount = float(input("Enter the total purchase amount: ruppees "))

# Step 3: Determine the discount based on the purchase amount
if purchase_amount >= 500:
    discount = 20  # 20% discount
elif purchase_amount >= 200:
    discount = 10  # 10% discount
else:
    discount = 0  # No discount

# Step 4: Calculate discount amount and final price
discount_amount = (discount / 100) * purchase_amount
final_price = purchase_amount - discount_amount

# Step 5: Display purchase summary
print("\n--- Purchase Summary ---")
print(f"Customer Name: {name}")
print(f"Total Purchase Amount: ${purchase_amount:.2f}")
print(f"Discount Percentage: {discount}%")
print(f"Discount Amount: rupees{discount_amount:.2f}")
print(f"Final Price to Pay: rupees{final_price:.2f}")

# Step 6: Additional feedback based on discount
if discount == 20:
    print("You got the highest discount! Thank you for shopping big!")
elif discount == 10:
    print("Good job! You qualify for a medium discount.")
else:
    print("No discount applied. Spend more next time to save money!")

# Step 7: Ask user if they want to add more items
print("\nWould you like to add more items to your purchase?")
response = input("Enter 'yes' or 'no': ").lower()

if response == "yes":
    extra_amount = float(input("Enter the amount for the additional items: rupees "))
    new_total = purchase_amount + extra_amount

    # Recalculate the discount
    if new_total >= 500:
        discount = 20
    elif new_total >= 200:
        discount = 10
    else:
        discount = 0

    discount_amount = (discount / 100) * new_total
    final_price = new_total - discount_amount

    # Display updated purchase summary
    print("\n--- Updated Purchase Summary ---")
    print(f"Customer Name: {name}")
    print(f"New Total Purchase Amount: ${new_total:.2f}")
    print(f"Discount Percentage: {discount}%")
    print(f"Discount Amount: rupees{discount_amount:.2f}")
    print(f"Final Price to Pay: rupees{final_price:.2f}")
else:
    print("Thank you for shopping with us! Have a great day!")

# Step 8: Final message
print("\n--- End of Program ---")








    









