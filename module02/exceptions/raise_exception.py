# raise — enforce a required environment variable
import os

try:
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise EnvironmentError("DATABASE_URL is not set.")
except EnvironmentError as e:
    print(f"Configuration error: {e}")
else:
    print(f"Connecting to: {db_url}")
    print("Connection established successfully.")
finally:
    print("Startup check complete.")
