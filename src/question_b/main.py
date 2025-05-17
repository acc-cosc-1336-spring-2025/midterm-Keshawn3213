def main():
    while True:
        try:
            user_input = input("Enter a number to sum the even numbers (or type 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
            num = int(user_input)
            result = get_sum_of_evens(num)
            print(f"The sum of even numbers from 1 to {num} is: {result}")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    main()
