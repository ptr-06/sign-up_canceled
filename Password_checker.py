def Secure_password(password):
    lowercase = False 
    uppercase = False
    special_character = False
    digit = False
    if len(password) < 8:
        return False
    for i in range(len(password)):
        if password[i].islower(): lowercase = True
        if password[i].isupper(): uppercase = True
        if password[i].isdigit(): digit = True
        if password[i] in "!@#$%^&*()": special_character = True
        if password.count(password[i]) > 2 or ord(password[i]) == ord(password[i-1]) + 1 == ord(password[i-2]) + 2:
            return False
    return lowercase and uppercase and special_character and digit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    password = "Dc@9150836"
    print(Secure_password(password))


