#Name checker programme. Possible to write name with lower and capital letters!
        
my_name = "linus"

name_checker = True

while name_checker:
    name_my = input("Type the name as is in the string\n")
    if name_my.lower() == my_name:
        print("Yes, that IS indeed my name :D")
        name_checker = False
    else:
        print("It is not that difficult to spell my name :/")
