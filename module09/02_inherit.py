# inheritance: child class extends and specialises a parent


class HTTPError(Exception):
    def __init__(self, status_code, message):
        super().__init__(message)
        self.status_code = status_code

    def response(self):
        return f"{self.status_code}: {self.args[0]}"


class NotFoundError(HTTPError):
    def __init__(self, resource):
        super().__init__(404, f"{resource} not found")


class UnauthorizedError(HTTPError):
    def __init__(self):
        super().__init__(401, "Authentication required")


class ForbiddenError(HTTPError):
    def __init__(self):
        super().__init__(403, "Access denied")


err = NotFoundError("User #42")
print(err.response())                   # 404: User #42 not found

print(isinstance(err, HTTPError))       # True  — child IS-A parent
print(isinstance(err, NotFoundError))   # True
print(isinstance(err, UnauthorizedError))  # False

print(type(err) is HTTPError)           # False — exact type check
print(type(err) is NotFoundError)       # True

print(dir(err))

print("--------------------")

# second example: User hierarchy
# child extends parent behaviour using super()


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet(self):
        return f"Hello, {self.username}"

    def can_delete(self):
        return False


class AdminUser(User):
    def __init__(self, username, email, department):
        super().__init__(username, email)   # reuse parent __init__
        self.department = department

    def greet(self):
        return f"{super().greet()} [Admin · {self.department}]"  # extend, not replace

    def can_delete(self):
        return True


user = User("alice", "alice@example.com")
admin = AdminUser("bob", "bob@example.com", "Engineering")

print(user.greet())     # Hello, alice
print(admin.greet())    # Hello, bob [Admin · Engineering]

print(user.can_delete())    # False
print(admin.can_delete())   # True

print(isinstance(admin, User))       # True — AdminUser IS-A User
print(isinstance(user, AdminUser))   # False
