from classes.payment import PaymentMethod
class CreditCard(PaymentMethod):
    def pay(self,amount):
        return f"CreditCard Succeeded {amount}!"
    def fee(self):
        return 2