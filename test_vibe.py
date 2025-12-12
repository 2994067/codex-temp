from datetime import datetime


def main() -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Hello! This is the vibe test script.")
    print(f"Current time: {now}")

    with open("vibe.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{now}] Script ran successfully.\n")


if __name__ == "__main__":
    main()
