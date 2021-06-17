# cardNumber = input('Enter Your Card No. : ')
# pin = input('Enter Your pin : ')
class Atm :
     def __init__(self, cardNo, pin,balance):
        self.cardNo = cardNo
        self.pin = pin
        self.balance = balance

     def checkBalace(self):
      print(self.balance)
     
     def withdraw(self) :
         amount = int(input('Enter the amount  : '))
         if amount > self.balance : 
            print('Insufficient Funds')
         else : 
            available =  self.balance - amount
            print('Transaction Succesfull')
            print('Available Balance : ' , available)

userBalace = 10000
cardNumber = input('Enter your card No. : ')
pin = input('Enter your pin : ')
choice = input('Would you like to withdraw, check balance : ')

atm = Atm(cardNumber,pin,userBalace)

if choice == 'withdraw' : 
    atm.withdraw()
elif choice == "check balance" or "checkbalance" : 
    atm.checkBalace()    
else :
    print('invailid Option')    
   
       
