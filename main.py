from classes.payment import PaymentMethod
from classes.CreditCard import CreditCard
from classes.PayPal import PayPal
def checkout(type_payment,amount):
    return type_payment.pay(amount)

for method in [CreditCard(), PayPal()]:
    print(checkout(method, 100))
