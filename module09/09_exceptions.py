# custom exception hierarchy: build specific, catchable error types
# inherit from a common base so callers can catch broadly or narrowly


class AppError(Exception):
    def __init__(self, message, code=None):
        super().__init__(message)
        self.code = code

    def __str__(self):
        prefix = f"[{self.code}] " if self.code else ""
        return f"{prefix}{super().__str__()}"


class DatabaseError(AppError):
    pass


class DBConnectionError(DatabaseError):
    def __init__(self, host):
        super().__init__(f"Cannot connect to {host}", code="DB_CONN")


class QueryError(DatabaseError):
    def __init__(self, query, reason):
        super().__init__(f"Query failed: {query!r} — {reason}", code="DB_QUERY")


class APIError(AppError):
    pass


class RateLimitError(APIError):
    def __init__(self, limit):
        super().__init__(f"Rate limit exceeded: {limit} req/min", code="RATE_LIMIT")


class AuthError(APIError):
    def __init__(self):
        super().__init__("Invalid or expired token", code="AUTH")


# catching by hierarchy: broad → narrow
errors = [
    DBConnectionError("db.prod.internal"),
    QueryError("SELECT * FROM users", "table does not exist"),
    RateLimitError(100),
    AuthError(),
]

for err in errors:
    print(err)

print("--------------------")

# real usage: catch only what you can handle
def fetch_user(user_id):
    raise QueryError(f"SELECT * FROM users WHERE id={user_id}", "connection lost")

try:
    fetch_user(42)
except QueryError as e:
    print(f"Retry query: {e}")
except DatabaseError as e:
    print(f"DB problem: {e}")
except AppError as e:
    print(f"App problem: {e}")
