from payment import PaymentMethod
class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"PayPal Succeeded {amount}"