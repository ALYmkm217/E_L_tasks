import pyfiglet

username = ['ahmed','ali','amr']
password = [1,2,3]

name = input ("please enter your user name : ")
pas = int (input ("please enter your password : "))


if name in username and pas in password :
    name_index= username.index(name)
    pas_index= password.index(pas)

    if name_index == pas_index:
        print('\nWelcome Buddy,', name.title(),'\n')
        pyname = pyfiglet.figlet_format(name.title())   
        print(pyname)

    else: 
        print("\n\nTRY ONTHER!!!!!\n\n")
else: 
    print("\n\nYOU ARE NOT WELCOMED!!!!!\n\n")
   