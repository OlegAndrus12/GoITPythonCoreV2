# KeyError — accessing a missing key in an API response
response = {
    "status": 200,
    "data": {"username": "alice"},
}

try:
    email = response["data"]["email"]
    print(f"Email: {email}")
except KeyError as e:
    print(f"Missing field in response: {e}")

# IndexError — reading beyond the end of a list
log_lines = ["Server started", "DB connected"]

try:
    print(log_lines[5])
except IndexError:
    print("Log line does not exist.")

# TypeError — passing wrong type to an operation
try:
    count = "5"
    print(f"Total: {count + 1}")
except TypeError:
    print("Cannot add a string and an integer. Convert first.")
