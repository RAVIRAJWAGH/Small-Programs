#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Atm:
    def __init__(self,balance,pin):
        import getpass
        self.balance=balance
        self.pin=pin
        self.menu()
        
    def menu(self):
        inp=input('''Hello how can help you...
        1.Enter 1 to set pin
        2.Enter 2 to check balance
        3.Enter 3 to deposite balance
        4.Enter 4 to withdraw balance''')
        if inp=='1':
            self.set_pin()
        elif inp=='2':
            self.check_balance()
        elif inp=='3':
            self.deposite_balance()
        else:
            self.withdraw_balance()
    
    def set_pin(self):
        self.pin=input('Enter new pin')
        print('Pin set succesfully...')
        
    def check_balance(self):
        p=input('Enter your pin....')
        if p==str(self.pin):
            print(self.balance)
        else:
            print('Invalid Pin')
    def deposite_balance(self):
        am=int(input('Enter amount to deposite...'))
        self.balance+=am
        print(f'Your current balance is {self.balance}')
    def withdraw_balance(self):
        pin = getpass.getpass(prompt='Enter your password: ')
        #print('Password entered:', pin)
        #pin=input('Enter your pin...')
        if pin==str(self.pin):  
            am1=int(input('Enter amount to withdraw...'))
            self.balance-=am1
            print(f'Your current balance is {self.balance}')
        else:
            print('Invalid pin')


# In[3]:


a=Atm(10000,1234)


# In[ ]:




