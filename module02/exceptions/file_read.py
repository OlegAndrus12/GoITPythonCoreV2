# finally — always runs, used for cleanup (closing the file)
file = None
try:
    file = open("config.txt")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("config.txt not found. Using default settings.")
finally:
    if file:
        file.close()
        print("File closed.")

# else — runs only when no exception was raised
try:
    file = open("/etc/hosts", "w")
    file.write("127.0.0.1 myapp.local")
except PermissionError:
    print("Permission denied. Run as administrator.")
else:
    print("Hosts file updated successfully.")
    file.close()
