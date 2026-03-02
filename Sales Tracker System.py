# Sales Tracker System

# Initialize sales list
sales = []

print("="*40)
print("     SALES TRACKER SYSTEM")
print("="*40)

# Main loop
while True:
    # Display menu
    print("\n1. View all sales")
    print("2. Add daily sale")
    print("3. Calculate total sales")
    print("4. Calculate average sale")
    print("5. Find best day")
    print("6. Find worst day")
    print("7. Show days above average")
    print("8. Exit")
    print("="*40)
    
    choice = input("\nChoice: ")
    
    # Option 1: View all sales
    if choice == "1":
        if len(sales) == 0:
            print("\nNo sales data yet!")
        else:
            print("\n--- Sales Data ---")
            for i in range(len(sales)):
                print(f"Day {i + 1}: ${sales[i]:.2f}")
            print(f"Total entries: {len(sales)}")
    
    # Option 2: Add daily sale
    elif choice == "2":
        # Check if we already have 7 sales
        if len(sales) >= 7:
            print("\nCannot add more than 7 days!")
        else:
            try:
                amount = float(input("Enter sale amount: $"))
                
                # Validate positive amount
                if amount <= 0:
                    print("Amount must be positive!")
                else:
                    sales.append(amount)
                    day_number = len(sales)
                    print(f"Added sale for Day {day_number}: ${amount:.2f}")
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    # Option 3: Calculate total sales
    elif choice == "3":
        if len(sales) == 0:
            print("\nNo sales data yet!")
        else:
            total = sum(sales)
            print(f"\nTotal sales: ${total:.2f}")
    
    # Option 4: Calculate average sale
    elif choice == "4":
        if len(sales) == 0:
            print("\nNo sales data yet!")
        else:
            average = sum(sales) / len(sales)
            print(f"\nAverage daily sale: ${average:.2f}")
    
    # Option 5: Find best day
    elif choice == "5":
        if len(sales) == 0:
            print("\nNo sales data yet!")
        else:
            best_amount = max(sales)
            best_day = sales.index(best_amount) + 1
            print(f"\nBest day: Day {best_day}")
            print(f"Amount: ${best_amount:.2f}")
    
    # Option 6: Find worst day
    elif choice == "6":
        if len(sales) == 0:
            print("\nNo sales data yet!")
        else:
            worst_amount = min(sales)
            worst_day = sales.index(worst_amount) + 1
            print(f"\nWorst day: Day {worst_day}")
            print(f"Amount: ${worst_amount:.2f}")
    
    # Option 7: Show days above average
    elif choice == "7":
        if len(sales) == 0:
            print("\nNo sales data yet!")
        else:
            average = sum(sales) / len(sales)
            above_average = []
            
            for i in range(len(sales)):
                if sales[i] > average:
                    above_average.append((i + 1, sales[i]))
            
            if len(above_average) == 0:
                print(f"\nNo days above average (${average:.2f})")
            else:
                print(f"\n--- Days Above Average (${average:.2f}) ---")
                for day, amount in above_average:
                    print(f"Day {day}: ${amount:.2f}")
                print(f"Count: {len(above_average)} days")
    
    # Option 8: Exit
    elif choice == "8":
        print("\nThank you for using Sales Tracker!")
        break
    
    # Invalid choice
    else:
        print("\nInvalid choice! Please enter 1-8.")
