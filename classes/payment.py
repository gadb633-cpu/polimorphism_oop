from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    @abstractmethod    
    def pay(self,amount):
        pass
    @abstractmethod
    def fee(self,amount):
        pass