import sys
import statistics_utils  # <--- IMPORT YOUR NEW MODULE HERE

def print_menu():
    """Displays the main menu options to the user."""
    print("\n" + "="*40)
    print("   PYSTAT-CLI: Statistical Toolkit")
    print("="*40)
    print("1. Calculate Mean")
    print("2. Calculate Variance")
    print("3. Exit")
    print("-" * 40)

def get_user_numbers():
    """Helper function to get a list of numbers from the user."""
    try:
        user_input = input("Enter numbers separated by spaces: ")
        data = [float(x) for x in user_input.split()]
        return data
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return []

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '3':
            print("\nExiting PyStat-CLI. Goodbye!")
            sys.exit()

        # Get data for options 1 and 2
        data = get_user_numbers()
        if not data:
            continue

        if choice == '1':
            result = statistics_utils.calculate_mean(data)
            print(f"\nResult: Mean = {result:.2f}")
            
        elif choice == '2':
            result = statistics_utils.calculate_variance(data)
            print(f"\nResult: Sample Variance = {result:.2f}")
            
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()