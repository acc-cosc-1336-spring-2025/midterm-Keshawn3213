from reverse_string import reverse_string

def main():
    while True:
        user_input = input("Enter a string to reverse (or type 'q' to quit): ")
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
        reversed_str = reverse_string(user_input)
        print(f"Reversed string: {reversed_str}")

if __name__ == "__main__":
    main()
