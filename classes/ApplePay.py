from classes.payment import PaymentMethod
class ApplePay(PaymentMethod):
    def pay(self,amount):
        return f"ApplePay Succeeded {amount}!"