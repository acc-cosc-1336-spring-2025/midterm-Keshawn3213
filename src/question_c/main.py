from get_bonus_pay_amount import get_bonus_pay_amount

def main():
    while True:
        try:
            user_input = input("Enter the sales amount (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            sales = float(user_input)
            bonus = get_bonus_pay_amount(sales)
            print(f"Bonus Pay Amount: {bonus}")
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'q' to quit.")

if __name__ == "__main__":
    main()
