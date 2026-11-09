from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    def __init__(self,name):
        self.name =name
    @abstractmethod    
    def pay(self,amount):
        pass