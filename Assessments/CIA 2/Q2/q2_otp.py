
# Q2 - OTP Verification

CORRECT_OTP = "123456"


def verify_with_while():
    print("\n--- WHILE LOOP ---")
    attempts = 0

    while attempts < 3:
        entered = input("Enter OTP: ")

        if entered.strip() == "":
            print("Blank entry. This will not count.")
            continue

        attempts += 1

        if entered == CORRECT_OTP:
            print("OTP verified successfully!")
            break

        print("Wrong OTP. Attempts used:", attempts)

    else:
        print("Account locked for 30 minutes.")


def verify_with_for():
    print("\n--- FOR LOOP ---")

    for attempt in range(3):
        entered = input("Enter OTP: ")

        if entered.strip() == "":
            print("Blank entry. This will not count.")
            continue

        if entered == CORRECT_OTP:
            print("OTP verified successfully!")
            break

        print("Wrong OTP. Attempts used:", attempt + 1)

    else:
        print("Account locked for 30 minutes.")


def verify_with_extra_attempts():
    print("\n--- EXTRA ATTEMPTS ---")
    security_answer = input("Answer security question (yes/no): ")

    max_attempts = 5 if security_answer.lower() == "yes" else 3
    attempts = 0

    while attempts < max_attempts:
        entered = input("Enter OTP: ")

        if entered.strip() == "":
            print("Blank entry. Not counted.")
            continue

        attempts += 1

        if entered == CORRECT_OTP:
            print("OTP verified successfully!")
            break

        print("Wrong OTP.")

    else:
        print("Account locked for 30 minutes.")


# Demonstrate pass
def pass_demo():
    print("\n--- PASS DEMONSTRATION ---")
    for number in range(1, 4):
        if number == 2:
            pass  # Placeholder: no action
        print("Number:", number)


# Recursive alternative
def verify_recursive(attempts_left):
    if attempts_left == 0:
        print("Account locked for 30 minutes.")
        return

    entered = input("Enter OTP: ")

    if entered.strip() == "":
        print("Blank entry. Not counted.")
        return verify_recursive(attempts_left)

    if entered == CORRECT_OTP:
        print("OTP verified successfully!")
        return

    print("Wrong OTP.")
    return verify_recursive(attempts_left - 1)


if __name__ == "__main__":
    print("1. While loop")
    print("2. For loop")
    print("3. Extra attempts")
    print("4. Pass demonstration")
    print("5. Recursive alternative")

    choice = input("Choose option: ")

    if choice == "1":
        verify_with_while()
    elif choice == "2":
        verify_with_for()
    elif choice == "3":
        verify_with_extra_attempts()
    elif choice == "4":
        pass_demo()
    elif choice == "5":
        verify_recursive(3)
    else:
        print("Invalid choice")
