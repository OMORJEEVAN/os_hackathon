from backend.services.process_manager import kill_process, get_process_by_pid


def kill_process_command():
    """
    Ask user for PID and kill the process
    """
    try:
        pid = int(input("Enter PID to kill: "))

        confirm = input(f"Are you sure you want to kill process {pid}? (y/n): ")

        if confirm.lower() != "y":
            print("Cancelled.")
            return

        result = kill_process(pid)
        print(result["message"] if "message" in result else result)

    except ValueError:
        print("Invalid PID. Please enter a number.")


def inspect_process_command():
    """
    Show details of a specific process
    """
    try:
        pid = int(input("Enter PID to inspect: "))

        result = get_process_by_pid(pid)

        if "error" in result:
            print(result["error"])
            return

        print("\n--- Process Details ---")
        for key, value in result.items():
            print(f"{key}: {value}")

    except ValueError:
        print("Invalid PID. Please enter a number.")