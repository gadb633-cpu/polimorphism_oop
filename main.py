from classes.payment import PaymentMethod
from classes.CreditCard import CreditCard
from classes.PayPal import PayPal
def checkout(type_payment,amount,fee):
    return f"{type_payment.pay(amount)} | fee:{fee}"

for method in [CreditCard(), PayPal()]:
    print(checkout(method, 100,method.fee()))
