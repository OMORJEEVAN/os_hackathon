from cli.ui import live_dashboard


def main():
    print("\n===== Smart Process Monitor =====")
    print("1. Start Live Dashboard")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        live_dashboard()

    elif choice == "2":
        print("Exiting...")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()