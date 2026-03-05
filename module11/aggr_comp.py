
from abc import ABC, abstractmethod

class Provider(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Provider(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PayPalProvider(Provider, Provider):
    def pay(self, amount):
        print(f"Paid ${amount} via Paypal")

class StripeProvider:
    def pay(self, amount):
        print(f"Paid ${amount} via Stripe")

# aggregation
class Checkout:
    def __init__(self, payment_provider: Provider):
        self.provider = payment_provider

    def process_payment(self, amount):
        self.provider.pay(amount)

# composition
class Checkout:
    def __init__(self):
        self.provider = StripeProvider()

    def process_payment(self, amount):
        self.provider.pay(amount)


paypal = PayPalProvider()
stripe = StripeProvider()

checkout = Checkout(paypal)
checkout.process_payment(100)


checkout = Checkout(stripe)
checkout.process_payment(100)




