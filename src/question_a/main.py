from use_local_variable import use_local_variable

def main():
    num = 100
    print(f"Before function call, num = {num}")
    use_local_variable(num)
    print(f"After function call, num = {num}")

if __name__ == "__main__":
    main()
