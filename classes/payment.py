from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    @abstractmethod    
    def pay(self,amount):
        pass
    def fee(self,amount):
        return 0