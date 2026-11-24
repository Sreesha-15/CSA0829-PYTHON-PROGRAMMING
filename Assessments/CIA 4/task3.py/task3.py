
import os
import tempfile


class InvalidRecord(Exception):
    """Raised when an attendance record is invalid."""


def parse_line(line):
    """Convert one attendance line into a validated tuple."""

    parts = line.strip().split(",")

    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    register_number = parts[0].strip()
    attendance_date = parts[1].strip()
    status = parts[2].strip().upper()

    if not register_number:
        raise InvalidRecord("register number is empty")

    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")

    return register_number, attendance_date, status


def summarise(path):
    present = 0
    absent = 0
    errors = []

    try:
        with open(path, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):

                if not line.strip():
                    continue

                try:
                    register_number, attendance_date, status = (
                        parse_line(line)
                    )

                except InvalidRecord as error:
                    errors.append((line_number, str(error)))
                    continue

                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1

    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Attendance file not found: {path}"
        ) from error

    except PermissionError as error:
        raise PermissionError(
            f"Cannot access attendance file: {path}"
        ) from error

    except UnicodeDecodeError as error:
        raise UnicodeError(
            f"Invalid UTF-8 encoding in file: {path}"
        ) from error

    finally:
        print("File processing attempt completed.")

    return present, absent, errors


if __name__ == "__main__":

    data = (
        "192311001,2026-10-08,P\n"
        "192311002,2026-10-08,A\n"
        "192311003,2026-10-08\n"
        "192311004,2026-10-08,L\n"
    )

    with tempfile.NamedTemporaryFile(
        "w",
        suffix=".csv",
        delete=False,
        encoding="utf-8"
    ) as tmp:
        tmp.write(data)
        temporary_file = tmp.name

    try:
        result = summarise(temporary_file)
        print(result)

    finally:
        if os.path.exists(temporary_file):
            os.remove(temporary_file)

    print("\nTESTING MISSING FILE")

    try:
        summarise("missing_attendance_file.csv")

    except FileNotFoundError as error:
        print("Handled:", error)
        print("Original cause:", type(error.__cause__).__name__)
