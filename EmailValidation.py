import re

email = input('Enter Your Email: ')
space = False
uppercase = False
other_case = False


if len(email) >= 6:
    if email[0].isalpha():
        if '@' in email and email.count('@') == 1:
            if (email[-4] == '.') ^ (email[-3] == '.'):
                for character in email:
                    if character.isspace():
                        s = True
                    elif character.isalpha():
                        if character == character.upper():
                            uppercase = True
                    elif character.isdigit():
                        continue
                    elif character in ['_', '.', '@']:
                        continue
                    else:
                        other_case = True

                if space:
                    print('Invalid Email!! ; it Contains spaces.')
                elif uppercase:
                    print('Invalid Email!! ; it Contains Uppercase.')
                elif other_case:
                    print('Invalid Email!!.3')
                else:
                    print("It's a Valid Email.")

    else:
        print('Invalid Email!!!.2')
else:
    print('Invalid Email!!!.1')





