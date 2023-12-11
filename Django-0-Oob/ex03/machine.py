from beverages import HotBeverage, Coffee, Chocolate, Tea, Cappuccino
import random


class CoffeeMachine():
    def __init__(self) -> None:
        pass

    usage = 0

    class EmptyCup(HotBeverage):
        def __init__(self, name="empty cup", price=0.9) -> None:
            super().__init__(name, price)
        
        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self, *args: object) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.usage = 0

    def serve(self, beverage:HotBeverage) -> HotBeverage:
        if self.usage == 10:
            raise CoffeeMachine.BrokenMachineException()
        self.usage += 1
        rand_int = random.randint(0, 1)
        if rand_int == 0:
            return self.EmptyCup()
        return beverage()


if __name__ == "__main__":
    cm = CoffeeMachine()
    for i in range(22):
        print(f"beverage {i + 1}")
        rand_int = random.randint(0, 3)
        try:
            match rand_int:
                case 0:
                    beverage = cm.serve(Coffee)
                case 1:
                    beverage = cm.serve(Chocolate)
                case 2:
                    beverage = cm.serve(Tea)
                case 3:
                    beverage = cm.serve(Cappuccino)
            print(beverage)
        except CoffeeMachine.BrokenMachineException as err:
            print(err)
            cm.repair()
