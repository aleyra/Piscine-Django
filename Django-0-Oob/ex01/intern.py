class Intern():
    def __init__(self, Name="My name? I'm nobody, an intern, I have no name."):
        self.Name = Name
    
    def __str__(self) -> str:
        return self.Name
    
    class Coffee():
        def __str__(self) -> str:
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I'm just an intern, I can't do that...") 
    
    def make_coffee(self):
        return self.Coffee()


def test_intern(name):
    if name == "":
        my_intern = Intern()
    else:
        my_intern = Intern(name)
    print(my_intern)
    if name != "":
        print(my_intern.make_coffee())
    else:
        try:
            my_intern.work()
        except Exception as err:
            print(err)



if __name__ == "__main__":
    test_intern("Marc")
    test_intern("")