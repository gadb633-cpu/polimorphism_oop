from classes.payment import PaymentMethod
from classes.CreditCard import CreditCard
from classes.PayPal import PayPal
def checkout(type_payment,amount):
    return f"{type_payment.pay(amount)} | fee:{type_payment.fee(100)}"

for method in [CreditCard(), PayPal()]:
    print(checkout(method, 100))
