def main():
    print("====================================")
    print("     PERSONAL EXPENSE TRACKER       ")
    print("====================================")
    print("Enter your expense amounts below.")
    print("Type 'q', 'quit', or 'exit' to finish and see the total.")
    print("------------------------------------")

    total = 0.0
    count = 0

    while True:
        user_input = input("Enter expense amount: ").strip()

        # Check for exit condition
        if user_input.lower() in ['q', 'quit', 'exit']:
            break

        # Validate and process the input
        try:
            expense = float(user_input)
            if expense < 0:
                print("⚠️ Please enter a positive amount.")
                continue
            
            # Accumulator pattern: total = total + expense
            total = total + expense
            count += 1
            print(f"Added: ${expense:.2f} | Current Total: ${total:.2f}")
            print("------------------------------------")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number or 'q' to quit.")
            print("------------------------------------")

    print("\n====================================")
    print("          SUMMARY REPORT            ")
    print("====================================")
    print(f"Total Items Logged : {count}")
    print(f"Total Spent        : ${total:.2f}")
    print("====================================")
    print("Thank you for using Expense Tracker!")

if __name__ == "__main__":
    main()
