from abc import ABC, abstractmethod


# the same domain, two relationship patterns:
#
# AGGREGATION  — Checkout receives a provider from outside (provider can exist without Checkout)
# COMPOSITION  — Checkout creates its own provider internally (provider lives and dies with Checkout)


class Provider(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PayPalProvider(Provider):
    def pay(self, amount):
        print(f"Paid ${amount} via PayPal")


class StripeProvider(Provider):
    def pay(self, amount):
        print(f"Paid ${amount} via Stripe")


# ------- aggregation -------
class CheckoutAggregation:
    def __init__(self, payment_provider):
        self.provider = payment_provider    # passed in — provider exists independently

    def process(self, amount):
        self.provider.pay(amount)


paypal = PayPalProvider()
stripe = StripeProvider()

c1 = CheckoutAggregation(paypal)
c1.process(100)

c2 = CheckoutAggregation(stripe)
c2.process(200)

# paypal and stripe objects live on after c1/c2 are gone


# ------- composition -------
class CheckoutComposition:
    def __init__(self):
        self.provider = StripeProvider()    # created here — tied to this Checkout

    def process(self, amount):
        self.provider.pay(amount)


c3 = CheckoutComposition()
c3.process(50)
