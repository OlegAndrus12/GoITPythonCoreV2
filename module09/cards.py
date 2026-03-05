from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, number: str, owner: str):
        if not self._luhn_valid(number):
            raise ValueError("Invalid card number (Luhn check failed)")

        self.number = number
        self.owner = owner

    def _luhn_valid(number: str) -> bool:
        digits = [int(d) for d in number if d.isdigit()]
        checksum = 0

        for i, d in enumerate(reversed(digits)):
            if i % 2:
                d *= 2
                if d > 9:
                    d -= 9
            checksum += d

        return checksum % 10 == 0

    # polymorphic interface
    @abstractmethod
    def pay(self, amount: float):
        raise NotImplementedError

    def __repr__(self):
        return f"{self.__class__.__name__}(****{self.number[-4:]}, {self.owner})"

class DebitCard(Card):
    def __init__(self, number: str, owner: str, balance: float = 0):
        super().__init__(number, owner)
        self.balance = balance

    def pay(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


class CreditCard(Card):
    def __init__(self, number: str, owner: str, limit: float):
        super().__init__(number, owner)
        self.limit = limit
        self.debt = 0  # how much you owe

    @property
    def available_credit(self):
        return self.limit - self.debt

    def pay(self, amount: float):
        if amount > self.available_credit:
            raise ValueError("Credit limit exceeded")
        self.debt += amount

    def repay(self, amount: float):
        self.debt -= amount  # can go negative (bank owes you)


cards = [
    DebitCard("4532015112830366", "Oleh", balance=500),
    CreditCard("4485275742308327", "Oleh", limit=2000),
]

for card in cards:
    card.pay(100)

print(cards[0].balance)          # 400
print(cards[1].debt)             # 100
print(cards[1].available_credit) # 1900