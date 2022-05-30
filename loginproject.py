import xml.etree.ElementTree as ET

SIGN_UP = "sign up"
sign_up = SIGN_UP.casefold()
EXIT = "exit"
exit = EXIT.casefold() 
a = "menu"
Menu = a.casefold()
li ="login"
li.casefold()
def menu():
    while True:
        line = input('> ')
        if line == exit:
            break
        elif line == sign_up:
            signup()
        elif line == Menu:
            menu() 
        elif line == li:
            login()
        else:
            print('Please enter a valid command, you can type help for the commands available.')
def signup():
    name = input('Enter your name:\n')
    uname = input("Enter your username:\n")
    dob = input("Enter your date of birth in (DD/MM/YYYY) format:\n")
    email = input("Enter your email:\n")
    phone = input("Enter your phone number:\n")
    
    if (len(phone)==10):
        pass   
    else:  
        print('You have entered the phone number incrorrectly, Kindly fill the form again.')
        signup()
    passCode = input("Enter your password atleast 8 digit:\n")
    xmlformat = '''
        <user username="'''+ uname +'''">
            <name>'''+name+'''</name>
            <dob>'''+dob+'''</dob>
            <password>'''+passCode+'''</password>
            <email>'''+email+'''</email>
            <phone>'''+phone+'''</phone>
        </user> </users></stuff>'''
    if(len(passCode) > 7):
        hello = open('D:\Coding\Python\Project\Login Project\passwords.txt','r')
        stri = hello.read()
        xml = stri.split()
        # print(xml)
        var = str()
        for i in xml:
            if '/users' not in i:
                var = var +' '+ i
            else:
                continue
        print()
        newvar = str()
        for x in var:
            # print(x)
            if (x !='>'):
                newvar = newvar + x
            else:
                newvar = newvar + x +'\n'
        # print(newvar)
        hello.close()
        pwords = open('D:\Coding\Python\Project\Login Project\passwords.txt','w')
        # print(xmlformat)
        # print('Welcome! Your account has been created now use log in command to login to your account.')
        pwords.write(newvar + xmlformat)
        pwords.close()
    else:
        print('Please make sure that your password is atleast 8 character password')
        signup()
def login():
    username = input('Enter your username:\n')
    password = input('Enter your password:\n')
    loginv = open('D:\Coding\Python\Project\Login Project\passwords.txt','r')
    logindata = loginv.read()
    api = ET.fromstring(logindata)
    list = api.findall('users/user')

    # print(api)
    loginv.close()
    xdict = dict()
    for item in list:


        # print('Username:',item.get('username'))
        # print('Name',item.find('name').text)
        # print('Email:',item.find('email').text)
        # print('Phone:',item.find('phone').text)
        # print('Date of Birth:',item.find('dob').text)


        xuname = item.get('username')
        xpassword = item.find('password').text
        xdict[xuname] = xpassword 
    print(xdict)
    print(xdict.keys())
    if username in xdict.keys(): #and password == xdict[username] :
        # print('Welcome',username,'how were you been?')
        pconfirm = xdict[username]
        if pconfirm == xdict[username]:
            print('Welcome')
    else:
        pass
menu()