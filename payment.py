from abc import ABC,abstractmethod
class Payment(ABC):
    def __init__(self,name,amount):
        self.name =name
        self.amount = amount
    @abstractmethod    
    def pay(self):
        pass
    
