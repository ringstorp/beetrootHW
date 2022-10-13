print("Enter your phone number, 10 digits: ")

phone_num = input()

if phone_num.isnumeric() is True and len(phone_num) == 10:
    print('This is a valid phone number!')
else:
    print('This is NOT a valid phone number!')
