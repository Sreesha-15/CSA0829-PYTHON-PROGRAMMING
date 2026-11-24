from pathlib import Path
import logging

BASE_DIR = Path(__file__).parent
INPUT_DIR = BASE_DIR / "daily_returns"
LOG_FILE = BASE_DIR / "returned_books.log"
ERROR_FILE = BASE_DIR / "library_errors.log"

logging.basicConfig(
    filename=ERROR_FILE,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
    force=True
)


def process_daily_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as source:
            records = source.readlines()

        with open(LOG_FILE, "a", encoding="utf-8") as log:
            for record in records:
                record = record.strip()

                if record:
                    log.write(record + "\n")

        print(f"Processed successfully: {file_path.name}")

    except FileNotFoundError:
        logging.exception("Daily return file was not found: %s", file_path)
        print(f"Error: File not found - {file_path.name}")

    except PermissionError:
        logging.exception("Permission denied while accessing: %s", file_path)
        print(f"Error: Permission denied - {file_path.name}")

    except UnicodeDecodeError:
        logging.exception("Encoding error while reading: %s", file_path)
        print(f"Error: Unable to decode - {file_path.name}")

    except OSError:
        logging.exception("Operating system error while processing: %s", file_path)
        print(f"Error: File operation failed - {file_path.name}")


def main():
    INPUT_DIR.mkdir(exist_ok=True)

    daily_files = [
        INPUT_DIR / "day1.txt",
        INPUT_DIR / "day2.txt",
        INPUT_DIR / "day3.txt",
        INPUT_DIR / "day4.txt"
    ]

    for file_path in daily_files:
        process_daily_file(file_path)

    print("\nLibrary log processing completed.")
    print(f"Book records saved in: {LOG_FILE.name}")
    print(f"Error details saved in: {ERROR_FILE.name}")


if __name__ == "__main__":
    main()