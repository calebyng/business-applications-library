# Business Discount Qualifier

# Display program title
print("=" * 40)
print("    DISCOUNT QUALIFICATION SYSTEM")
print("=" * 40)
print()

# Get customer name, purchase amount, and loyalty status
customer_name = input("Enter customer name: ")
purchase_amount = float(input("Enter purchase amount: $"))
is_loyalty_member = input("Is customer a loyalty member? (yes/no): ").lower()

# Initialize discount variables
loyalty_discount = 0
birthday_discount = 0
volume_discount = 0
senior_discount = 0
first_time_discount = 0

# Determine loyalty discount based on years of membership and purchase amount
if is_loyalty_member == "yes":
    years_member = int(input("How many years as a member?: "))
    if years_member >= 5 and purchase_amount > 100:
        loyalty_discount = 20
    elif 2 <= years_member <= 4 and purchase_amount > 100:
        loyalty_discount = 15
    elif 0 <= years_member <= 1 and purchase_amount > 150:
        loyalty_discount = 10
        

# Check for birthday month discount
is_birthday = input("Is it their birthday month? (yes/no): ").lower()
if is_birthday == "yes":
        birthday_discount = 5

# Check for first-time customer discount
is_first_time = input("Is this their first purchase? (yes/no): ").lower()
if is_first_time == "yes" and is_loyalty_member == "no":
    first_time_discount = 10
else:
    first_time_discount = 0

# Check if customer qualifies for senior discount
age = int(input("Enter customer age: "))
if age >= 65:
        senior_discount = 5

# Determine volume discount based on purchase amount
if loyalty_discount == 0:
    if purchase_amount > 500:
        volume_discount = 25  
    elif purchase_amount > 300:
        volume_discount = 15  
    elif purchase_amount > 150:
        volume_discount = 10 
else:
    volume_discount = 0

# Sum all applicable discounts
total_discount = (loyalty_discount + birthday_discount +
                  volume_discount + senior_discount + first_time_discount)

# Cap total discount at 35%
if total_discount > 35:
    total_discount = 35

# Calculate discount amount and final price
discount_amount = (total_discount / 100) * purchase_amount
final_price = purchase_amount - discount_amount

# Display Discount Breakdown
print()
print("=" * 40)
print("         DISCOUNT BREAKDOWN")
print("=" * 40)

# Display Customer Name and Original Amount 
print(f"Customer: {customer_name}")
print(f"Original Amount: ${purchase_amount:.2f}")
print("Discounts Applied:")

# Check each discount one by one 
if loyalty_discount > 0:
    print(f"- Loyalty Member Discount: {loyalty_discount}%")
if birthday_discount > 0:
    print(f"- Birthday Bonus: 5%")
if first_time_discount > 0:
    print(f"- First-Time Customer: 10%")
if senior_discount > 0:
    print(f"- Senior Discount: 5%")
if volume_discount > 0:
    print(f"- Volume Discount: {volume_discount}%")

# Final Totals 
print("-" * 24) # Creates the divider line 
print(f"Total Discount: {total_discount}%")
print(f"Discount Amount: ${discount_amount:.2f}") 
print(f"Final Price: ${final_price:.2f}") 
print("Thank you for shopping with us!") 