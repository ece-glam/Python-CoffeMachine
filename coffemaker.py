class Coffee:
    def __init__(self,mv,ca,wv,sa):
        self.name=""
        self.milkVolume=mv
        self.coffeeAmount=ca
        self.waterVolume=wv
        self.sugarAmount=sa

class CoffeeMachine:
    def __init__(self):
        self.preference=""
        self.power=True

    def demand(self):
        print("choose your coffe choice: latte<1>, espresso<2>, flat white<3>, cappucino<4>, settings<5>, on/off<6>")

    def choose(self):
        self.preference=int(input("choose:"))
        if self.preference == 1:
            print("Latte is being prepared for you")
        elif self.preference==2:
            print("Espresso is being prepared for you")
        elif self.preference==3:
            print("Flat white is being prepared for you")
        elif self.preference==4:
            print("Cappucino is being prepared for you")
        elif self.preference==5:
            print("1.Cal-Clean, 2. Water Temp")
            num=int(input("Gir:"))
            if num==1:
                self.clean()
            elif num==2:
                self.termometer()

        elif self.preference == 6:
            print("Machine is shut down.")
            self.power = False

    def clean(self):
        rinse=Coffee(0,0,1000,0)
        print(" Machine was cleaned")
    
    def termometer(self):
        print("Water temperature is increased by 5 degree")

        
    def makeCoffee(self):
        if self.preference == 1:
            myCoffee = Coffee(200,4,50,0)
            myCoffee.name = "Latte"
        elif self.preference==2:
            myCoffee = Coffee(0,6,55,0)
            myCoffee.name = "Espresso"
        elif self.preference==3:
            myCoffee = Coffee(150,8,50,0)
            myCoffee.name = "Flat White"
        elif self.preference==4:
            myCoffee = Coffee(100,6,50,10)
            myCoffee.name = "Cappucino"
        return myCoffee
    

def main():
    myCoffeeMachine = CoffeeMachine()

    while True:
        myCoffeeMachine.demand()
        myCoffeeMachine.choose()
        if myCoffeeMachine.power == False:
            break
        elif myCoffeeMachine.preference==(1 or 2 or 3 or 4):
            yourCoffee = myCoffeeMachine.makeCoffee()
            print(yourCoffee.name+ " was prepared")
    


if __name__ == "__main__":
    main()
