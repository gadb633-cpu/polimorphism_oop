from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    def __init__(self,name,amount):
        self.name =name
        self.amount = amount
    @abstractmethod    
    def pay(self):
        pass