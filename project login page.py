def login():
    name = input('Enter your full name:\n')
    passnum = (input('Enter your password'))
    def phone():
        num = int(input('Enter your phone number:\n'))  
        digit = 0 
        while(digit < 0):
            digit = 1
            num = digit//10
        if len(num) == 10:
         pass
        else:
            print('The phone number is wrong')
            phone()
    phone()
    def password():
        if len(passnum==8):
            pass
        else:
            print("The password should be atleast eight characeters.")
        password()
    password()
login()