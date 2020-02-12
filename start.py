from random import randint

class Account:

    
    def __init__(self, card_number, amount, currancy):
        self.__card_number = card_number
        self.__amount = amount
        self.__currancy = currancy
        print("Account constructor")

    def show_info(self):
        print("Card number: ", self.__card_number, "\nAmount ", self.__amount, "\nCurrency ", self.__currancy)

    def get_money(self, amount_minus):
        if self.__amount >= amount_minus:
            self.__amount = self.__amount - amount_minus
            print("Card number: ", self.__card_number, "\nYou got money: ",  
                amount_minus,"\nAccount balance: ", self.__amount, "\nCurrency ", self.__currancy)
        else:
            print("Not enough money in the account")
            print("You can cash: ", self.__amount)
        

    def add_money(self, amount_plus):
        self.__amount = self.__amount + amount_plus
        print("Card number: ", self.__card_number, "\nAmount ", self.__amount, "\nCurrency ", self.__currancy)

exit = False
while not exit:
    print("+++++++++++++++MiniBank Cayman Islands+++++++++++++++++++++++++++++")
    try:
        choise = int(input(" 1. create account\n 2. get money\n 3. add money\n 0. exit\n"))
        if choise == 1:
            amount = int(input("Enter money ===> "))
            currancy = input("Enter curency: UAH, USD, EUR ===> ")
            card_number = randint(1000000, 9999999)
            credit_card = Account(card_number, amount, currancy)
            credit_card.show_info()
        elif choise == 2:
            amount_minus = int(input("Enter money  get===> "))
            credit_card.get_money(amount_minus)
        elif choise == 3:
            amount_plus = int(input("Enter money  add===> "))
            credit_card.add_money(amount_plus)        
        elif choise == 0:
            exit = True
        else:
            print("read manual")
    except Exception as error:
        print("ERROR ===> ", error)





