import re


def simple_calculator():
    print("--- Simple Expression Calculator ---")
    print("Type any math problem (e.g., 5 + 6 + 7 - 6) and press Enter.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter calculation: ")

        # Check if the user wants to quit
        if user_input.lower().strip() == "exit":
            print("Goodbye!")
            break

        # Remove all spaces to make checking easier
        cleaned_input = user_input.replace(" ", "")

        # Security check: Only allow numbers and basic math operators (+, -, *, /, .)
        if not re.match(r"^[\d+\-*/.]+$", cleaned_input):
            print(
                "Invalid input! Please use only numbers and operators (+, -, *, /).\n"
            )
            continue

        try:
            # Calculate the result
            result = eval(cleaned_input)

            # Display the original input followed by the result
            print(f"{user_input} = {result}\n")

        except ZeroDivisionError:
            print("Error: You cannot divide by zero!\n")
        except Exception:
            print("Oops, that wasn't a valid math expression. Try again!\n")


if __name__ == "__main__":
    simple_calculator()
