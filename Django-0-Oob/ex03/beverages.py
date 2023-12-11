class HotBeverage():
    def __init__(self, name="hot beverage", price=0.30) -> None:
        self.name = name
        self.price = price

    def description(self):
        return "Just some hot water in a cup."

    def __str__(self) -> str:
        return f"""name : {self.name}
price : {self.price:.2f}
description : {self.description()}"""
    

class Coffee(HotBeverage):
    def __init__(self, name="coffee", price=0.40) -> None:
        super().__init__(name, price)
    
    def description(self):
        return "A coffee, to stay awake."
    

class Tea(HotBeverage):
    def __init__(self, name="tea") -> None:
        super().__init__(name)
    
    def description(self):
        return "Just some hot water in a cup."
    

class Chocolate(HotBeverage):
    def __init__(self, name="chocolate", price=0.50) -> None:
        super().__init__(name, price)
    
    def description(self):
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self, name="cappuccino", price=0.45) -> None:
        super().__init__(name, price)
    
    def description(self):
        return "Un po' di Italia nella sua tazza!"


if __name__ == "__main__":
    hb = HotBeverage()
    print(hb)
    coffee = Coffee()
    print(coffee)
    tea = Tea()
    print(tea)
    choco = Chocolate()
    print(choco)
    cappu = Cappuccino()
    print(cappu)
