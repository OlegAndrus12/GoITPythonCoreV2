# composition: the outer object CREATES and OWNS the inner object
# the inner object cannot exist on its own — its lifetime is tied to the outer one


class InstagramAccount:
    def __init__(self, username):
        self.username = username
        self.followers = 0

    def info(self):
        return f"Instagram @{self.username} ({self.followers} followers)"


class FacebookAccount:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.instagram = InstagramAccount(name)  # created automatically, owned by Facebook

    def info(self):
        return f"Facebook: {self.name} <{self.email}>"


account = FacebookAccount("john_doe", "john@example.com")

print(account.info())
print(account.instagram.info())

# there is no standalone InstagramAccount here — it was created inside FacebookAccount
