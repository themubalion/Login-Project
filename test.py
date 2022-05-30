import xml.etree.ElementTree as ET


Hello = open('D:\Coding\Python\Project\Login Project\passwords.txt','r')
helo = Hello.read()
# print(helo)
hi = ET.fromstring(helo)
Hi = hi.findall('users/user')
for i in Hi:
    print(i.find('password').text)