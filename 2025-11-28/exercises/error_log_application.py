from datetime import datetime

def error_log(message):
    with open("error.log", "a") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}]\tError: {message}\n")
        print("Error logged!")

for i in range(5):
    message = int((input("\nEnter 1 for WARNING, 2 for CRITICAL or 3 for INFO: ")))
    error_log("WARNING" if message == 1 else "CRITICAL" if message == 2 else "INFO")
