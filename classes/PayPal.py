from classes.payment import PaymentMethod
class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"PayPal Succeeded {amount}!"
    def fee(self,fee):
        return fee