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
print(var)
newvar = str()
for x in var:
    # print(x)
    if (x !='>'):
        newvar = newvar + x
    else:
        newvar = newvar + x +'\n'
print(newvar)