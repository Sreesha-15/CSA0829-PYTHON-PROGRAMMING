
from decimal import Decimal, InvalidOperation
from pathlib import Path


def process_mess_bill(filename):
    total = Decimal("0.00")
    report = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):

                if not line.strip():
                    continue

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected exactly 3 fields")

                    register_number = parts[0].strip()
                    name = parts[1].strip()
                    amount_text = parts[2].strip()

                    if not register_number or not name:
                        raise ValueError("Register number or name is empty")

                    try:
                        amount = Decimal(amount_text)
                    except InvalidOperation as error:
                        raise ValueError("Invalid amount") from error

                    if not amount.is_finite() or amount < 0:
                        raise ValueError("Amount must be a non-negative number")

                    total += amount
                    report.append(
                        f"{register_number}, {name}, Rs.{amount:.2f}"
                    )

                except ValueError as error:
                    rejected.append(
                        f"Line {line_number}: {line.strip()} | {error}"
                    )

    except FileNotFoundError:
        print("ERROR: Input file was not found.")
        return

    except PermissionError:
        print("ERROR: Permission denied while opening the file.")
        return

    except UnicodeDecodeError:
        print("ERROR: File encoding is not valid UTF-8.")
        return

    else:
        print("MESS BILL REPORT")
        print("-" * 45)

        for record in report:
            print(record)

        print("-" * 45)
        print(f"Total Mess Bill: Rs.{total:.2f}")

        print("\nREJECTED RECORDS")

        if rejected:
            for record in rejected:
                print(record)
        else:
            print("No rejected records.")

    finally:
        print("\nFile processing completed.")


if __name__ == "__main__":
    input_file = Path(__file__).parent / "mess_oct.txt"
    process_mess_bill(input_file)
