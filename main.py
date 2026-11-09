from classes.payment import PaymentMethod
from classes.CreditCard import CreditCard
from classes.PayPal import PayPal
from classes.Character import Character
from classes.Mage import Mage
from classes.Warrior import Warrior
# exe 1,2
def checkout(type_payment,amount):
    return f"{type_payment.pay(amount)} | fee:{type_payment.fee(100)}"

for method in [CreditCard(), PayPal()]:
    print(checkout(method, 100))

# exe 3
def attack(validity,attacked):
    attacked.health -=validity.attack_power()
    print(f"{validity.name} hits {attacked.name} for {validity.attack_power()}")

conan = Warrior("Conan", 100)
merlin = Mage("Merlin", 60)
attack(conan, merlin)
attack(merlin, conan)
print(merlin.name, merlin.health)
print(conan.name, conan.health)

# exe 4
# 1. yes, because they have the same method 
# 2. polymorphism without the inherent